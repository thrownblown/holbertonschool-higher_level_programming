#!/usr/bin/node
class Rectangle {
  // non empty rectangle class
  constructor (w, h) {
    // no longer useless
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // prints the rectangle using the character X
    for (let row = 0; row < this.height; row++) {
      let x = '';
      for (let col = 0; col < this.width; col++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  rotate () {
    // that exchanges the width and the height of the rectangle
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    // that multiples the width and the height of the
    this.height = this.height * 2;
    this.width = this.width * 2;
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

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
