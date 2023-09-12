#!/usr/bin/node
const FirstSquare = require('./5-square');

class Square extends FirstSquare {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      let temp = this.height;
      while (temp > 0) {
        console.log('C'.repeat(this.width));
        temp--;
      }
    }
  }
}
module.exports = Square;
