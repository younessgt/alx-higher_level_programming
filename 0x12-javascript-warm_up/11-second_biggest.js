#!/usr/bin/node
const arg = process.argv;
/* sort the number in ascending order */
const numArr = arg.slice(2).sort((a, b) => a - b);
const len = numArr.length;
if (arg.length <= 3) {
  console.log(0);
} else {
  console.log(numArr[len - 2]);
}
