#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) { return console.log(err); }
  let bdy = JSON.parse(body);
  const includer = (acc, item) => acc + item.includes('18/');
  const reducer = (acc, item) => acc + item.characters.reduce(includer, 0);
  console.log(bdy.results.reduce(reducer, 0));
});
