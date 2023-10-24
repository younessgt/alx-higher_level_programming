#!/usr/bin/node

const request = require('request');
let count = 0;
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    for (const obj of results) {
      const characters = obj.characters;
      for (const character of characters) {
        if (character.includes('18')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
