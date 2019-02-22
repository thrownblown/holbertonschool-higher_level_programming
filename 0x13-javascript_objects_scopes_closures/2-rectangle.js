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
}

module.exports = Rectangle;
