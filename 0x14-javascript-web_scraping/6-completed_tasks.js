#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  if (!err && response.statusCode === 200) {
    const data = JSON.parse(body);
    const result = {};
    for (const obj of data) {
      if (obj.completed) {
        if (result[obj.userId]) {
          result[obj.userId] += 1;
        } else {
          result[obj.userId] = 1;
        }
      }
    }
    console.log(result);
  }
});
