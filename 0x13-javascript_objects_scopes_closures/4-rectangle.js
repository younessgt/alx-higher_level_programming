#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let temp = this.height;
    while (temp > 0) {
      console.log('X'.repeat(this.width));
      temp--;
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temp1 = this.height;
    this.height = this.width;
    this.width = temp1;
  }
}
module.exports = Rectangle;
