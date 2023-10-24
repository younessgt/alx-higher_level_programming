#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
fs.readFile(args[2], 'utf-8', (err, content) => {
  if (err) {
    console.error(err);
  } else {
    console.log(content);
  }
});
