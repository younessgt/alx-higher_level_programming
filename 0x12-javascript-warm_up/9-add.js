#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const arg = process.argv;
const nm1 = parseInt(arg[2], 10);
const nm2 = parseInt(arg[3], 10);
const x = add(nm1, nm2);
console.log(x);
