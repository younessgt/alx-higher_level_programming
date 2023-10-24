#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, content) => {
  if (content) {
    console.log(content);
  } else {
    console.error(err);
  }
});
