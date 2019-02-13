#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let arr = process.argv.slice(2, process.argv.length);
  arr = arr.map(item => Number(item));
  arr.sort((a, b) => a - b);
  console.log(arr[arr.length - 2]);
  console.log(arr);
}
