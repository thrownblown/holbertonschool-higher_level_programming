#!/usr/bin/node
const fileSys = require('fs');
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) { return console.log(err); }
  fileSys.writeFile(process.argv[3], body, (err) => {
    if (err) console.log(err);
  });
});


