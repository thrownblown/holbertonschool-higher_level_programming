#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) { return console.log(err); }
  let ret = {};
  JSON.parse(body).forEach(item => {
    if (item.completed) {
      ret[item.userId] ? ret[item.userId] += 1 : ret[item.userId] = 1;
    }
  });
  console.log(ret);
});
