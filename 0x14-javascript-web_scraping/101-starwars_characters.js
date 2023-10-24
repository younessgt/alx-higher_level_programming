#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    /* defining a function "process" to process a character at a given index 'i' */
    const process = (i) => {
      if (i < data.characters.length) {
        request(data.characters[i], (err, response, body) => {
          if (err) {
            console.error(err);
          } else {
            const data2 = JSON.parse(body);
            console.log(data2.name);
          }
          process(i + 1);
        });
      }
    };
    process(0);
  }
});
