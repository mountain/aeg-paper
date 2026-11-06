// Separate process entry: neither imports nor invokes the producer/test generator.
import {receive} from './receive.mjs';
import {contract,readJSON} from './io.mjs';
import {canonical,demand} from './common.mjs';
try {
  demand(process.argv.length===4,'usage:receive-cli packet.json expected-request');
  const result=receive(readJSON(process.argv[2]),process.argv[3],contract());
  process.stdout.write(canonical(result)+'\n');
} catch(e) {process.stderr.write('REJECTED: '+e.message+'\n');process.exitCode=1;}
