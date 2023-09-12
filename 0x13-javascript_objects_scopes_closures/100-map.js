#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const listF = list.map((current, index) => current * index);
console.log(listF);
