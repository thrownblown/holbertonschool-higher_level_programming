#!/usr/bin/node
let fileSys = require('fs');
fileSys.readFile(process.argv[2], { encoding: 'utf-8' }, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
