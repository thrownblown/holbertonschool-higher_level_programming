#!/usr/bin/node

class Rectangle {
  // emppty rectangle class
  constructor (w, h) {
    // no longer useless
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row < this.height; row++) {
      let x = '';
      for (let col = 0; col < this.width; col++) {
        x += 'X';
      }
      console.log(x);
    }
  }
}

module.exports = Rectangle;
