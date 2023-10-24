#!/usr/bin/node

const fs = require('fs');

const args = process.argv;

fs.readFile(args[2], 'utf8', (err, content) => {
  if (content) {
    console.log(content);
  } else {
    console.log(err);
  }
});
