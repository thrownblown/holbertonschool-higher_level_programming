#!/usr/bin/node
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
// If an error occurred during while writing, print the error object
let fileSys = require('fs');

fileSys.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) console.log(err);
});
