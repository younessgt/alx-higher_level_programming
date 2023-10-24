#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    for (const urlCharacter of data.characters) {
      request(urlCharacter, (err, response, body) => {
        if (err) {
          console.error(err);
        }
        const data2 = JSON.parse(body);
        console.log(data2.name);
      });
    }
  }
});
