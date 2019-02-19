#!/usr/bin/node
let oldDict = require('./101-data.js');

let newDict = {};

for (let key in oldDict.dict) {
  if (newDict[oldDict.dict[key]]) {
    newDict[oldDict.dict[key]].push(key);
  } else {
    newDict[oldDict.dict[key]] = [key];
  }
}

console.log(newDict);
