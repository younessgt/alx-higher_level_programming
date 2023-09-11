#!/usr/bin/node
const arg = process.argv;
const numArr = arg.slice(2).sort();
const len = numArr.length;
if (arg.length <= 3) {
  console.log(0);
} else {
  console.log(numArr[len - 2]);
}
