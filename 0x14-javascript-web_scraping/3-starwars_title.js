#!/usr/bin/node
// Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
// The first argument is the episode number
// You must use the Star wars API with the endpoint http://swapi.co/api/films/:id
// You must use the module request
const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], (err, res, body) => {
  if (err) { return console.log(err); }
  console.log(JSON.parse(body).title);
});
