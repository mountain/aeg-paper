import {readFileSync,writeFileSync,mkdtempSync,rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {resolve} from 'node:path';
import {spawnSync} from 'node:child_process';
import {canonical,demand,clone,strictJSON} from './common.mjs';
import {root,contract,readJSON,pins} from './io.mjs';
import {run,checkEvidence,rejection} from './verify.mjs';
const c=contract(),p=pins();
function check(file) {return checkEvidence(readJSON(file),c,p);}
function selftest() {
  const file=resolve(root,'evidence-v3.json'),e=readJSON(file);
  checkEvidence(e,c,p);
  const temp=mkdtempSync(resolve(tmpdir(),'oq096-v3-'));
  const tests=[];
  for(const row of e.cases.filter(x=>x.verdict==='accepted'))
    tests.push({name:row.request,key:row.request,packet:row.left,accepted:true});
  for(const row of e.negatives)
    tests.push({name:row.name,key:row.expected,packet:row.packet,accepted:false,code:row.code});
  let nodeCount=0,pythonCount=0;
  try {
    for(const [i,t] of tests.entries()) {
      const path=resolve(temp,i+'.json');writeFileSync(path,canonical(t.packet)+'\n');
      const child=spawnSync(process.execPath,[resolve(root,'receive-cli.mjs'),path,t.key],{encoding:'utf8'});
      demand(!child.error&&child.status===(t.accepted?0:1),'fresh:node:'+t.name+':'+child.stderr);
      if(!t.accepted)demand(child.stderr.trim()==='REJECTED: '+t.code,'fresh:node-reason:'+t.name);
      nodeCount++;
      const py=spawnSync(process.env.PYTHON||'python3',[resolve(root,'oracle.py'),'--packet',path,t.key],{encoding:'utf8'});
      demand(!py.error&&py.status===(t.accepted?0:1),'fresh:python:'+t.name+':'+py.stderr);
      pythonCount++;
    }
    const changed=clone(e);changed.summary.accepted=999;
    demand(rejection(()=>checkEvidence(changed,c,p))==='evidence:recalculation','evidence:forged-summary');
    const reordered=clone(e);[reordered.cases[0],reordered.cases[1]]=[reordered.cases[1],reordered.cases[0]];
    demand(rejection(()=>checkEvidence(reordered,c,p))==='evidence:order','evidence:order-control');
    const replaced=clone(e);replaced.cases[0].left=e.cases[2].left;
    demand(rejection(()=>checkEvidence(replaced,c,p))==='request:binding','evidence:foreign');
    const lost=clone(e);lost.cases[0].left.graph.guards=[];
    demand(rejection(()=>checkEvidence(lost,c,p))==='domain:guard','evidence:guard-control');
    const rehashed=clone(e),l=rehashed.cases[0].left.graph.leaves.find(x=>x.port==='Q:x:in');
    l.source='C:x';l.record=clone(c.source_registry['C:x']);
    demand(rejection(()=>checkEvidence(rehashed,c,p))==='source:binding','evidence:same-value-source');
    // Source integrity is semantic: there is no self-asserted packet digest to trust.
    for(const text of ['{"x":1,"x":2}','{"x":{"a":1,"\\u0061":2}}']) {
      const path=resolve(temp,'duplicate.json');writeFileSync(path,text);
      const child=spawnSync(process.execPath,[resolve(root,'receive-cli.mjs'),path,'A'],{encoding:'utf8'});
      demand(child.status===1&&child.stderr.trim()==='REJECTED: json:duplicate-key','fresh:duplicate-json');
    }
    return {node_fresh_packets:nodeCount,python_fresh_packets:pythonCount,
      evidence_mutations_rejected:5,duplicate_json_rejected:2,summary:e.summary};
  } finally {rmSync(temp,{recursive:true,force:true});}
}
try {
  const mode=process.argv[2];
  if(mode==='generate')process.stdout.write(canonical({schema:'oq096-evidence-v3',pins:p,...run(c)})+'\n');
  else if(mode==='check')process.stdout.write(canonical(check(process.argv[3]||resolve(root,'evidence-v3.json')))+'\n');
  else if(mode==='selftest')process.stdout.write(canonical(selftest())+'\n');
  else throw new Error('usage: cli.mjs generate|check [evidence.json]|selftest');
} catch(e) {process.stderr.write('REJECTED: '+e.message+'\n');process.exitCode=1;}
