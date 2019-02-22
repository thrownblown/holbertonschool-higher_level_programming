#!/usr/bin/node

function sortNumber (a, b) {
  return a - b;
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let arr = process.argv.slice(2, process.argv.length);
  arr = arr.map(Number);
  arr.sort(sortNumber);
  console.log(arr[arr.length - 2]);
}
