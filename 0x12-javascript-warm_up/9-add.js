#!/usr/bin/node
let a = Number(process.argv[2]);
let b = Number(process.argv[3]);

let add = (a, b) => a + b;

let retval = add(a, b);
console.log(retval);
