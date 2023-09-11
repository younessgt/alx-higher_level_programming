#!/usr/bin/node

const arg = process.argv;
let num = parseInt(arg[2], 10);
const size = num;
if (isNaN(num)) {
  console.log('Missing size');
} else if (!isNaN(num) && num > 0) {
  while (num > 0) {
    console.log('X'.repeat(size));
    num--;
  }
}
