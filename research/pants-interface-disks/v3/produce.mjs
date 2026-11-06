import {demand,clone,arithmetic,request,role,equal} from './common.mjs';

function normalize(g,c) {
  g.events.sort((a,b)=>a.key.localeCompare(b.key));
  g.ports.sort((a,b)=>a.role.localeCompare(b.role));
  g.leaves.sort((a,b)=>a.port.localeCompare(b.port));
  g.bindings.sort((a,b)=>a.from.localeCompare(b.from));
  g.guards.sort((a,b)=>a.event.localeCompare(b.event));
  const inbound=new Set(g.bindings.map(e=>e.to)), outbound=new Set(g.bindings.map(e=>e.from));
  const order=c.blocks.flatMap(b=>b.inputs.map(w=>role(b.key,w,'in')));
  const outputs=c.blocks.map(b=>role(b.key,b.output,'out'));
  g.boundary={inputs:order.filter(p=>g.ports.some(o=>o.role===p)&&!inbound.has(p)),
    outputs:outputs.filter(p=>g.ports.some(o=>o.role===p)&&!outbound.has(p))};
  return g;
}
export function leaf(block,key,c) {
  const r=request(key,c), b=c.blocks.find(b=>b.key===block);
  const inputs=b.inputs.map(w=>role(b.key,w,'in')),output=role(b.key,b.output,'out');
  const event={key:b.key,id:r.scope+'/'+b.event,source:b.source,op:b.op,inputs,output,type:b.type};
  const ports=[...inputs.map((p,i)=>({role:p,id:r.scope+'/'+p,event:b.key,direction:'in',slot:i,type:b.type})),
    {role:output,id:r.scope+'/'+output,event:b.key,direction:'out',slot:0,type:b.type}];
  const assignments={...c.fixed_sources,'Q:x:in':r.inputs.x,'Q:y:in':r.inputs.y};
  const leaves=inputs.filter(p=>p in assignments).map(port=>({port,source:assignments[port],
    record:clone(c.source_registry[assignments[port]]),occurrence:r.scope+'/'+port}));
  return normalize({events:[event],ports,bindings:[],leaves,
    guards:b.op==='div'?[{event:b.key,denominator:inputs[1],nonzero:true}]:[],boundary:{}},c);
}
export function compose(down,up,c) {
  const ids=[...up.ports,...down.ports,...up.events,...down.events].map(x=>x.id);
  demand(new Set(ids).size===ids.length,'compose:identity-collision');
  const roles=[...up.events,...down.events].map(x=>x.key);
  demand(new Set(roles).size===roles.length,'compose:event-collision');
  const us=new Set(up.ports.map(x=>x.role)),ds=new Set(down.ports.map(x=>x.role));
  demand(!c.bindings.some(e=>ds.has(e.from)&&us.has(e.to)),'compose:reverse');
  const fresh=c.bindings.filter(e=>us.has(e.from)&&ds.has(e.to));
  demand(fresh.length>0,'compose:no-interface');
  const allports=[...up.ports,...down.ports];
  const wires=fresh.map(e=>({...clone(e),from_id:allports.find(p=>p.role===e.from).id,
    to_id:allports.find(p=>p.role===e.to).id}));
  const g={};
  for(const k of ['events','ports','leaves','guards'])g[k]=clone([...up[k],...down[k]]);
  g.bindings=clone([...up.bindings,...down.bindings,...wires]);
  return normalize(g,c);
}
export function construct(key,side,c) {
  const q=leaf('Q',key,c),p=leaf('P',key,c),r=leaf('R',key,c);
  demand(['left','right'].includes(side),'compose:side');
  return side==='left'?compose(compose(r,p,c),q,c):compose(r,compose(p,q,c),c);
}
export function evaluateGraph(g) {
  // Producer schedule is chosen by readiness, independently of array ordering.
  const values=Object.fromEntries(g.leaves.map(l=>[l.port,l.record.value]));
  const pending=[...g.events],trace=[];
  while(pending.length) {
    for(const e of g.bindings)if(e.from in values)values[e.to]=values[e.from];
    const i=pending.findIndex(e=>e.inputs.every(p=>p in values));
    demand(i>=0,'producer:blocked');
    const e=pending.splice(i,1)[0],args=e.inputs.map(p=>values[p]);
    const result=arithmetic(e.op,...args);values[e.output]=result;
    trace.push({event:e.key,id:e.id,source:e.source,op:e.op,inputs:args,output:result});
  }
  return {trace,numeric:{z:values['Q:z:out'],w:values['P:w:out'],v:values['R:v:out']}};
}
export function packet(key,side,c) {
  const r=request(key,c),graph=construct(key,side,c);
  return {schema:'oq096-receipt-v3',request:key,scope:r.scope,graph,...evaluateGraph(graph)};
}
export function lastSeamOnly(key,side,c) {
  // A closed defective algebra on (numeric partial function, interval, last seam).
  // The function carries no source/occurrence observation; only the seam survives.
  const req=request(key,c);
  const atom=(name,fn)=>({first:name,last:name,fn,ledger:[]});
  const q=atom('Q',xy=>arithmetic('add',xy[0],xy[1]));
  const p=atom('P',z=>arithmetic('mul',z,'4'));
  const r=atom('R',w=>arithmetic('div','1',w));
  function bad(d,u) {
    const b=c.bindings.find(e=>e.from.startsWith(u.last+':')&&e.to.startsWith(d.first+':'));
    demand(!!b,'bad:nonadjacent');
    return {first:u.first,last:d.last,fn:x=>d.fn(u.fn(x)),
      ledger:[{...clone(b),from_id:req.scope+'/'+b.from,to_id:req.scope+'/'+b.to}]};
  }
  const out=side==='left'?bad(bad(r,p),q):bad(r,bad(p,q));
  const xy=[c.source_registry[req.inputs.x].value,c.source_registry[req.inputs.y].value];
  const z=q.fn(xy),w=p.fn(z);
  return {numeric:{z,w,v:out.fn(xy)},ledger:out.ledger};
}
