// Exact arithmetic and representation helpers only; no producer/receiver calls.
export function demand(ok, reason) { if (!ok) throw new Error(reason); }
export function canonical(x) {
  if (Array.isArray(x)) return '[' + x.map(canonical).join(',') + ']';
  if (x !== null && typeof x === 'object')
    return '{' + Object.keys(x).sort().map(k => JSON.stringify(k)+':'+canonical(x[k])).join(',') + '}';
  return JSON.stringify(x);
}
export const equal = (a,b) => canonical(a) === canonical(b);
export const clone = x => JSON.parse(JSON.stringify(x));
export function fields(x, names, reason) {
  demand(x !== null && typeof x === 'object' && !Array.isArray(x)
    && equal(Object.keys(x).sort(), names.split(' ').sort()), reason);
}
function gcd(a,b) { a = a<0n?-a:a; while(b) { [a,b]=[b,a%b]; } return a; }
export function fraction(n,d=1n) {
  demand(d!==0n,'domain:zero'); if(d<0n) { n=-n; d=-d; }
  const g=gcd(n,d); n/=g; d/=g; return d===1n?String(n):n+'/'+d;
}
export function parse(s) {
  demand(typeof s==='string' && s.length<=80 && /^-?(0|[1-9][0-9]*)(\/[1-9][0-9]*)?$/.test(s),'number:format');
  const a=s.split('/'), n=BigInt(a[0]),d=BigInt(a[1]||'1');
  demand(fraction(n,d)===s,'number:canonical'); return [n,d];
}
export function arithmetic(op,a,b) {
  const [n,d]=parse(a),[m,e]=parse(b);
  if(op==='add')return fraction(n*e+m*d,d*e);
  if(op==='mul')return fraction(n*m,d*e);
  demand(op==='div','event:operation'); return fraction(n*e,d*m);
}
export function request(key,c) {
  let r=c.instances.find(x=>x.key===key);
  if(!r) {
    const m=/^grid:([0-5]):([0-5])$/.exec(key);
    demand(!!m,'request:unknown');
    r={key,scope:'run-'+key.replaceAll(':','-'),inputs:{x:'grid:'+c.grid[+m[1]],y:'grid:'+c.grid[+m[2]]}};
  }
  return clone(r);
}
export function keys(c) {
  return [...c.instances.map(x=>x.key),...c.grid.flatMap((_,i)=>c.grid.map((_,j)=>'grid:'+i+':'+j))];
}
export const role=(b,w,d)=>b+':'+w+':'+d;
export function strictJSON(s) {
  demand(typeof s==='string'&&s.length<2000000,'json:size');
  // JSON.parse loses repeated object keys; reject them in a token pass first.
  const tokens=s.match(/"(?:\\[\s\S]|[^"\\])*"|[{}\[\]:,]|-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?|true|false|null/g)||[];
  let p=0;
  function val() {
    const t=tokens[p++];
    if(t==='{') {
      const seen=new Set();
      if(tokens[p]==='}') {p++;return;}
      while(true) {
        const k=tokens[p++]; demand(k?.startsWith('"'),'json:syntax');
        const name=JSON.parse(k); demand(!seen.has(name),'json:duplicate-key'); seen.add(name);
        demand(tokens[p++]===':','json:syntax'); val();
        const end=tokens[p++]; if(end==='}')break; demand(end===',','json:syntax');
      }
    } else if(t==='[') {
      if(tokens[p]===']') {p++;return;}
      while(true) {val();const end=tokens[p++];if(end===']')break;demand(end===',','json:syntax');}
    } else demand(t!==undefined&&!['}',']',':',','].includes(t),'json:syntax');
  }
  val();demand(p===tokens.length,'json:syntax');
  try { return JSON.parse(s); } catch { throw new Error('json:syntax'); }
}
