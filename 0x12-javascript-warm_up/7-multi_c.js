#!/usr/bin/node
const arg = process.argv;
let num = parseInt(arg[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else if (!isNaN(num) && num > 0) {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
