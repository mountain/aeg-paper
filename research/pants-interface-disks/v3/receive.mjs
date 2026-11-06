// Does not import produce.mjs. Same author; separate code is not independent review.
import {demand,fields,equal,clone,arithmetic,parse,request,role} from './common.mjs';

export function topological(g) {
  const names=g.events.map(e=>e.key),ports=new Map(g.ports.map(p=>[p.role,p]));
  const incoming=new Map(names.map(k=>[k,0])),after=new Map(names.map(k=>[k,[]]));
  for(const b of g.bindings) {
    const a=ports.get(b.from),z=ports.get(b.to);
    demand(a&&z&&a.direction==='out'&&z.direction==='in','binding:endpoints');
    demand(after.has(a.event)&&incoming.has(z.event),'binding:event');
    after.get(a.event).push(z.event);incoming.set(z.event,incoming.get(z.event)+1);
  }
  const ready=names.filter(k=>incoming.get(k)===0).sort(),order=[];
  while(ready.length) {
    const k=ready.shift();order.push(k);
    for(const v of after.get(k)) {incoming.set(v,incoming.get(v)-1);
      if(incoming.get(v)===0) {ready.push(v);ready.sort();}}
  }
  demand(order.length===names.length,'graph:feedback');return order;
}
export function validateGraph(g,key,c) {
  const r=request(key,c);
  fields(g,'events ports bindings leaves guards boundary','graph:fields');
  for(const k of ['events','ports','bindings','leaves','guards'])
    demand(Array.isArray(g[k]),'graph:arrays');
  demand(g.events.length===3&&equal(g.events.map(e=>e.key),['P','Q','R']),'event:inventory');
  for(const e of g.events) {
    fields(e,'key id source op inputs output type','event:fields');
    const b=c.blocks.find(b=>b.key===e.key);
    demand(e.source===b.source,'event:source');
    demand(e.op===b.op&&equal(e.inputs,b.inputs.map(w=>role(b.key,w,'in')))
      &&e.output===role(b.key,b.output,'out')&&e.type===b.type,'event:shape');
  }
  const wantPorts=c.blocks.flatMap(b=>[
    ...b.inputs.map((w,i)=>({role:role(b.key,w,'in'),event:b.key,direction:'in',slot:i,type:b.type})),
    {role:role(b.key,b.output,'out'),event:b.key,direction:'out',slot:0,type:b.type}]);
  demand(g.ports.length===9&&equal(g.ports.map(p=>p.role),wantPorts.map(p=>p.role).sort()),'port:inventory');
  for(const p of g.ports) {
    fields(p,'role id event direction slot type','port:fields');
    demand(Number.isInteger(p.slot),'port:slot-type');
    const w=wantPorts.find(o=>o.role===p.role);
    demand(p.type===w.type,'port:type');
    demand(p.event===w.event&&p.direction===w.direction&&p.slot===w.slot,'port:slot-or-role');
  }
  const ids=[...g.events,...g.ports].map(x=>x.id);
  demand(ids.every(x=>typeof x==='string')&&new Set(ids).size===12,'identity:collision');
  for(const e of g.events)demand(e.id===r.scope+'/'+c.blocks.find(b=>b.key===e.key).event,'identity:scope');
  for(const p of g.ports)demand(p.id===r.scope+'/'+p.role,'identity:scope');
  const ports=new Map(g.ports.map(p=>[p.role,p]));
  for(const b of g.bindings) {
    fields(b,'from to output_slot input_slot type from_id to_id','binding:fields');
    demand(Number.isInteger(b.output_slot)&&Number.isInteger(b.input_slot),'binding:slot-type');
    const p=ports.get(b.from),q=ports.get(b.to);
    demand(p&&q&&p.direction==='out'&&q.direction==='in','binding:endpoints');
    demand(b.type===p.type&&b.type===q.type,'binding:type');
    demand(b.output_slot===p.slot&&b.input_slot===q.slot,'binding:slot');
    demand(b.from_id===p.id&&b.to_id===q.id&&b.from_id!==b.to_id,'binding:identity');
  }
  const order=topological(g); // Full graph, before fixed-chain binding comparison.
  demand(g.bindings.length===2,'binding:inventory');
  demand(new Set(g.bindings.map(e=>e.from)).size===2&&new Set(g.bindings.map(e=>e.to)).size===2,'binding:linearity');
  const wanted=[...c.bindings].sort((a,b)=>a.from.localeCompare(b.from));
  demand(equal(g.bindings.map(({from_id,to_id,...b})=>b),wanted),'binding:plan');
  fields(g.boundary,'inputs outputs','boundary:fields');
  demand(equal(g.boundary,{inputs:c.external_order,outputs:c.output_order}),'boundary:binding');
  demand(g.leaves.length===4&&equal(g.leaves.map(l=>l.port),[...c.external_order].sort()),'leaf:inventory');
  const assignments={...c.fixed_sources,'Q:x:in':r.inputs.x,'Q:y:in':r.inputs.y};
  for(const l of g.leaves) {
    fields(l,'port source record occurrence','leaf:fields');
    demand(typeof l.source==='string'&&Object.hasOwn(c.source_registry,l.source),'source:unknown');
    demand(equal(l.record,c.source_registry[l.source]),'source:record');
    demand(l.source===assignments[l.port],'source:binding');
    demand(l.occurrence===ports.get(l.port).id,'source:occurrence');
    parse(l.record.value);
  }
  demand(equal(g.guards,[{event:'R',denominator:'R:w:in',nonzero:true}]),'domain:guard');
  return order;
}
export function replay(g,key,c) {
  const order=validateGraph(g,key,c),values=new Map(g.leaves.map(l=>[l.port,l.record.value]));
  const incoming=new Map(g.bindings.map(b=>[b.to,b.from])),trace=[];
  for(const k of order) {
    const e=g.events.find(e=>e.key===k),args=e.inputs.map(p=>{
      const v=values.get(incoming.get(p)||p);demand(v!==undefined,'history:unbound');return v;});
    const out=arithmetic(e.op,args[0],args[1]);values.set(e.output,out);
    trace.push({event:e.key,id:e.id,source:e.source,op:e.op,inputs:args,output:out});
  }
  return {trace,numeric:{z:values.get('Q:z:out'),w:values.get('P:w:out'),v:values.get('R:v:out')}};
}
export function observe(p) {
  const g=clone(p.graph);
  g.events=g.events.map(({id,...e})=>e);
  g.ports=g.ports.map(({id,...o})=>o);
  g.leaves=g.leaves.map(({occurrence,...l})=>l);
  g.bindings=g.bindings.map(({from_id,to_id,...b})=>b);
  return {graph:g,trace:p.trace.map(({id,...e})=>e),numeric:p.numeric};
}
export function receive(p,key,c) {
  const r=request(key,c);
  fields(p,'schema request scope graph trace numeric','packet:fields');
  demand(p.schema==='oq096-receipt-v3','packet:schema');
  demand(p.request===key&&p.scope===r.scope,'request:binding');
  const actual=replay(p.graph,key,c);
  demand(equal(p.trace,actual.trace),'history:replay');
  demand(equal(p.numeric,actual.numeric),'numeric:replay');
  return {numeric:actual.numeric,source:observe(p)};
}
