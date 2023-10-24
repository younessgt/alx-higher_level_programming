#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, content) => {
  if (content) {
    console.log(content);
	return;
  } else {
    console.error(err);
  }
});
