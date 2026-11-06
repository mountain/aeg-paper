import {demand,equal,clone,keys,request,canonical,arithmetic,strictJSON} from './common.mjs';
import {packet,construct,leaf,compose,evaluateGraph,lastSeamOnly} from './produce.mjs';
import {receive,replay,observe,topological} from './receive.mjs';

export function rejection(fn) { try {fn();} catch(e) {return e.message;} return 'ACCEPTED'; }
function requireReason(fn,code) {const got=rejection(fn);demand(got===code,'test:expected:'+code+':got:'+got);}
function rename(p,from,to) {return JSON.parse(JSON.stringify(p).replaceAll(from,to));}
function edge(g,from,to) {
  const a=g.ports.find(p=>p.role===from),b=g.ports.find(p=>p.role===to);
  return {from,to,output_slot:a.slot,input_slot:b.slot,type:a.type,from_id:a.id,to_id:b.id};
}
export function mutations(c) {
  const a=packet('A','left',c),out=[];
  function add(name,code,edit) {const p=clone(a);edit(p);out.push({name,expected:'A',code,packet:p});}
  add('same-value-source','source:binding',p=>{
    const l=p.graph.leaves.find(l=>l.port==='Q:x:in');l.source='C:x';l.record=clone(c.source_registry['C:x']);});
  add('changed-origin','source:record',p=>p.graph.leaves[1].record.origin='invented');
  add('unknown-source','source:unknown',p=>p.graph.leaves[1].source='missing');
  add('changed-gate-source','event:source',p=>p.graph.events[0].source='Q:add');
  add('collapsed-seam-occurrences','identity:collision',p=>{
    p.graph.ports.find(o=>o.role==='P:z:in').id=p.graph.ports.find(o=>o.role==='Q:z:out').id;});
  add('event-port-collision','identity:collision',p=>p.graph.events[0].id=p.graph.ports[0].id);
  add('wrong-scope','identity:scope',p=>p.graph.ports[0].id='foreign/'+p.graph.ports[0].role);
  add('boolean-slot','binding:slot-type',p=>p.graph.bindings[0].input_slot=true);
  add('wrong-R-slot','binding:slot',p=>p.graph.bindings[0].input_slot=0);
  add('boolean-port-slot','port:slot-type',p=>p.graph.ports[0].slot=false);
  add('changed-type','port:type',p=>p.graph.ports[0].type='integer');
  add('missing-old-seam','binding:inventory',p=>p.graph.bindings.pop());
  add('duplicate-seam','binding:linearity',p=>p.graph.bindings[1]=clone(p.graph.bindings[0]));
  add('extra-fanout','binding:inventory',p=>p.graph.bindings.push(edge(p.graph,'Q:z:out','R:u:in')));
  add('feedback','graph:feedback',p=>p.graph.bindings.push(edge(p.graph,'R:v:out','Q:x:in')));
  add('self-loop','graph:feedback',p=>p.graph.bindings.push(edge(p.graph,'P:w:out','P:z:in')));
  add('deleted-producer','event:inventory',p=>p.graph.events=p.graph.events.filter(e=>e.key!=='Q'));
  add('swapped-Q-slots','event:shape',p=>p.graph.events.find(e=>e.key==='Q').inputs.reverse());
  add('missing-trace','history:replay',p=>p.trace.shift());
  add('changed-trace','history:replay',p=>p.trace[0].inputs=['1','4']);
  add('dropped-guard','domain:guard',p=>p.graph.guards=[]);
  add('misbound-guard','domain:guard',p=>p.graph.guards[0].denominator='R:u:in');
  add('wrong-boundary','boundary:binding',p=>p.graph.boundary.inputs.reverse());
  add('unbound-input','leaf:inventory',p=>p.graph.leaves.pop());
  add('unrecorded-discard','boundary:binding',p=>p.graph.boundary.outputs=[]);
  add('missing-residual','graph:fields',p=>p.graph={});
  add('changed-output','numeric:replay',p=>p.numeric.v='1/21');
  add('wrong-source-occurrence','source:occurrence',p=>p.graph.leaves[0].occurrence=p.graph.ports[1].id);
  out.push({name:'foreign-request',expected:'A',code:'request:binding',packet:packet('B','left',c)});
  const rewritten=rename(packet('C','left',c),'run-C','run-A');rewritten.request='A';
  out.push({name:'renamed-foreign-source',expected:'A',code:'source:binding',packet:rewritten});
  const copy=packet('A-copy','left',c);
  copy.request='A';copy.scope='run-A';
  out.push({name:'copy-with-stale-occurrences',expected:'A',code:'identity:scope',packet:copy});
  const zeroKey='grid:2:2',z=construct(zeroKey,'left',c);
  out.push({name:'zero-denominator',expected:zeroKey,code:'domain:zero',
    packet:{schema:'oq096-receipt-v3',request:zeroKey,scope:request(zeroKey,c).scope,graph:z,trace:[],numeric:{z:'0',w:'0',v:'0'}}});
  return out;
}
export function sourceAudit(c) {
  let accepted=0,rejected=0,unchanged=0;
  const registered=Object.keys(c.source_registry).sort();
  for(const item of c.instances) {
    const base=packet(item.key,'left',c);
    for(const sx of registered)for(const sy of registered) {
      const p=clone(base);
      for(const [port,s] of [['Q:x:in',sx],['Q:y:in',sy]]) {
        const l=p.graph.leaves.find(l=>l.port===port);l.source=s;l.record=clone(c.source_registry[s]);
      }
      // Rebuild all arithmetic claims without asking receiver which sources are legal.
      const numerical=rejection(()=>Object.assign(p,evaluateGraph(p.graph)));
      if(numerical!=='ACCEPTED')demand(numerical==='domain:zero','audit:numeric-error');
      const legal=sx===item.inputs.x&&sy===item.inputs.y,verdict=rejection(()=>receive(p,item.key,c));
      if(legal){demand(verdict==='ACCEPTED','audit:legal');accepted++;}
      else {demand(verdict==='source:binding','audit:foreign');rejected++;
        if(numerical==='ACCEPTED'&&equal(p.numeric,base.numeric))unchanged++;}
    }
  }
  return {attempted:accepted+rejected,accepted,rejected,numeric_unchanged_rejected:unchanged};
}
export function edgeAudit(c) {
  const base=packet('A','left',c),rows=[];
  for(const a of base.graph.ports.filter(p=>p.direction==='out'))
    for(const b of base.graph.ports.filter(p=>p.direction==='in')) {
      const p=clone(base);p.graph.bindings.push(edge(p.graph,a.role,b.role));
      const topology=rejection(()=>topological(p.graph)),verdict=rejection(()=>receive(p,'A',c));
      demand(['ACCEPTED','graph:feedback'].includes(topology),'audit:topology');
      demand(verdict!=='ACCEPTED','audit:extra-edge-admitted');
      rows.push({from:a.role,to:b.role,topology,reception:verdict});
    }
  return rows;
}
export function run(c) {
  const cases=[],identities=new Set();let good=0,zero=0;
  for(const key of keys(c)) {
    const leftGraph=construct(key,'left',c),rightGraph=construct(key,'right',c);
    demand(equal(leftGraph,rightGraph),'test:graph-associativity');
    for(const obj of [...leftGraph.events,...leftGraph.ports]) {
      demand(!identities.has(obj.id),'test:cross-request-freshness');identities.add(obj.id);
    }
    const l=rejection(()=>replay(leftGraph,key,c)),r=rejection(()=>replay(rightGraph,key,c));
    demand(l===r,'test:domain-associativity');
    if(l==='domain:zero') {
      zero++;cases.push({request:key,verdict:l,left_graph:leftGraph,right_graph:rightGraph});
      requireReason(()=>packet(key,'left',c),'domain:zero');
      requireReason(()=>packet(key,'right',c),'domain:zero');
    } else {
      demand(l==='ACCEPTED','test:unexpected-replay:'+l);
      const left=packet(key,'left',c),right=packet(key,'right',c);
      demand(equal(left,right),'test:packet-associativity');
      const lo=receive(left,key,c),ro=receive(right,key,c);
      demand(equal(lo,ro),'test:observation-associativity');
      cases.push({request:key,verdict:'accepted',left,right});good++;
    }
  }
  demand(good===36&&zero===5,'test:case-count');
  const a=packet('A','left',c),copy=packet('A-copy','left',c);
  demand(!equal(a,copy)&&equal(observe(a),observe(copy)),'test:fresh-source-reuse');
  demand(!equal(observe(a),observe(packet('C','left',c))),'test:same-operand-source-separation');
  requireReason(()=>compose(leaf('Q','A',c),leaf('Q','A',c),c),'compose:identity-collision');
  requireReason(()=>compose(leaf('Q','A',c),leaf('P','A',c),c),'compose:reverse');
  const negatives=mutations(c);
  for(const n of negatives)requireReason(()=>receive(n.packet,n.expected,c),n.code);
  const left=lastSeamOnly('A','left',c),right=lastSeamOnly('A','right',c);
  demand(equal(left.numeric,right.numeric)&&!equal(left.ledger,right.ledger),'test:lossy-witness');
  for(const side of [left,right]) {
    const p=clone(a);p.graph.bindings=side.ledger;
    requireReason(()=>receive(p,'A',c),'binding:inventory');
  }
  const edges=edgeAudit(c),sources=sourceAudit(c);
  requireReason(()=>strictJSON('{"a":1,"a":2}'),'json:duplicate-key');
  requireReason(()=>strictJSON('{"a":{"x":1,"\\u0078":2}}'),'json:duplicate-key');
  return {cases,negatives,counterexample:{left,right},
    summary:{requests:cases.length,accepted:good,domain_rejected:zero,
      bracketed_constructions:2*cases.length,distinct_occurrences:identities.size,
      source_reuse_alpha_equal:true,source_audit:sources,
      negative_packets:negatives.length,extra_edges:edges.length,
      cyclic_extra_edges:edges.filter(x=>x.topology==='graph:feedback').length},
    edge_audit:edges};
}
export function checkEvidence(e,c,pins) {
  demand(equal(e.pins,pins),'evidence:pins');
  demand(e.schema==='oq096-evidence-v3','evidence:schema');
  demand(Array.isArray(e.cases)&&e.cases.length===keys(c).length,'evidence:inventory');
  for(let i=0;i<e.cases.length;i++) {
    const row=e.cases[i],key=keys(c)[i];demand(row.request===key,'evidence:order');
    if(row.verdict==='accepted') {
      receive(row.left,key,c);receive(row.right,key,c);
      demand(equal(row.left,row.right),'evidence:brackets');
    } else {
      demand(row.verdict==='domain:zero','evidence:verdict');
      requireReason(()=>replay(row.left_graph,key,c),'domain:zero');
      requireReason(()=>replay(row.right_graph,key,c),'domain:zero');
      demand(equal(row.left_graph,row.right_graph),'evidence:brackets');
    }
  }
  // Check supplied packets first; reconstruction alone must not hide corruption.
  for(const n of e.negatives)requireReason(()=>receive(n.packet,n.expected,c),n.code);
  demand(equal(e,{schema:'oq096-evidence-v3',pins,...run(c)}),'evidence:recalculation');
  return e.summary;
}
