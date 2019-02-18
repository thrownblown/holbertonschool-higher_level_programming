#!/usr/bin/node
exports.esrever = function (list) {
  let ret = [];
  for (let i = list.length - 1; i >= 0; i--) {
    ret.push(list[i]);
  }
  return ret;
};
