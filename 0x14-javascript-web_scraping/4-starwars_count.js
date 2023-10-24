#!/usr/bin/node

const request = require('request');
let count = 0;
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  if (!err && response.statusCode === 200) {
    const data = JSON.parse(body);
    const results = data.results;
    for (const obj of results) {
      const characters = obj.characters;
      for (const character of characters) {
        const url2 = 'https://swapi-api.alx-tools.com/api/people/18/';
        if (character === url2) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
