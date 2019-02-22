#!/usr/bin/node
let OldSquare = require('./5-square');

class Square extends OldSquare {
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    // prints the rectangle using the character X
    if (c === undefined) {
      c = 'X';
    }
    for (let row = 0; row < this.height; row++) {
      let x = '';
      for (let col = 0; col < this.width; col++) {
        x += c;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
