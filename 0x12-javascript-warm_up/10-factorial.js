#!/usr/bin/node
function factorial (x) {
  if (isNaN(x) || x === 0 || x === 1) {
    return 1;
  } else if (x < 0) {
    return -1;
  }
  return (x * factorial(x - 1));
}
const arg = process.argv;
const num = parseInt(arg[2], 10);
const result = factorial(num);
console.log(result);
