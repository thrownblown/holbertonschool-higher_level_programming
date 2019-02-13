#!/usr/bin/node
if (!process.argv[2]) {
  console.log('No arguments');
} else if (process.argv[3]) {
  console.log(process.argv[3]);
}
