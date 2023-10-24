#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  if (!err && response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
