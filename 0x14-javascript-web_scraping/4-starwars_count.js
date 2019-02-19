#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) { return console.log(err); }
  let bdy = JSON.parse(body);
  const reducer = (acc, item) => acc + item.characters.includes('https://swapi.co/api/people/18/');
  console.log(bdy.results.reduce(reducer, 0));
});
