#!/usr/bin/node
// let list = require('./100-data.js');

console.log(list);

const multiIndex = (num, idx) => num * idx;

let newList = list.map(multiIndex);

console.log(newList);
