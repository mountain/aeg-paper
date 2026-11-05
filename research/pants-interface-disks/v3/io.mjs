import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {dirname,resolve} from 'node:path';
import {demand,strictJSON} from './common.mjs';
export const root=dirname(fileURLToPath(import.meta.url));
export const contractBlob='704655355b4ae69f9b11bd7dc7b7451e696de460';
export const pinFiles=["SPEC.md","common.mjs","produce.mjs","receive.mjs","verify.mjs","io.mjs","cli.mjs","receive-cli.mjs","oracle.py"];
export function gitBlob(path) {
  const bytes=readFileSync(path);
  return createHash('sha1').update('blob '+bytes.length+'\0').update(bytes).digest('hex');
}
export function readJSON(path) {return strictJSON(readFileSync(path,'utf8'));}
export function contract() {
  demand(gitBlob(resolve(root,'contract.json'))===contractBlob,'contract:pin');
  const c=readJSON(resolve(root,'contract.json')),repo=resolve(root,'../../..');
  for(const [path,sha] of Object.entries(c.frozen_files))
    demand(gitBlob(resolve(repo,path))===sha,'frozen:changed:'+path);
  return c;
}
export function pins() {
  return {contract_git_blob:contractBlob,
    implementation_git_blobs:Object.fromEntries(pinFiles.map(p=>[p,gitBlob(resolve(root,p))]))};
}
