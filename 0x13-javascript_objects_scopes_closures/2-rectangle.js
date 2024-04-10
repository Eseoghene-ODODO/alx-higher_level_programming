#!/usr/bin/node
/*
 * A class Rectangle that defines a rectangle
 */

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined || w <= 0 || h <= 0) {
      // do nothing
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
