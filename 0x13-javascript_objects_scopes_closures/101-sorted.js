#!/usr/bin/node
const dict = require('./101-data').dict;

const Dict = {};
for (const key in dict) {
  if (Dict[dict[key]] === undefined) {
    Dict[dict[key]] = [];
  }
  Dict[dict[key]].push(key);
}

console.log(Dict);
