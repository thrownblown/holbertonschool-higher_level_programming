#!/usr/bin/node
let fileSys = require('fs');
let fileA = fileSys.readFileSync('./' + process.argv[2]);
let fileB = fileSys.readFileSync('./' + process.argv[3]);
fileSys.writeFileSync(process.argv[4], fileA + fileB);
