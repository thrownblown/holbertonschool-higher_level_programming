#!/usr/bin/node
let myNumb = Math.floor(process.argv[2]);
if (!myNumb || isNaN(myNumb)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNumb);
}
