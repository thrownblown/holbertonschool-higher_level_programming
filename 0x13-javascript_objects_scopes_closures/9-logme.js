#!/usr/bin/node
let ret = 0;
exports.logMe = (item) => console.log(ret++ + ': ' + item);
