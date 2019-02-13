#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('No arguments');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else if (process.argv.length > 3) {
  console.log('Arguments found');
}
for (let j = 0; j < process.argv.length; j++) {
  console.log(j + ' -> ' + (process.argv[j]));
}
