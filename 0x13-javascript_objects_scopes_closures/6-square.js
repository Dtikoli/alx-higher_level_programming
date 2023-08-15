#!/usr/bin/node

const PSquare = require('./5-square');

class Square extends PSquare {
  charPrint (c) {
    c = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
