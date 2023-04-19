#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);
    const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
    let count = 0;
    for (let i = 0; result.results[i] !== undefined; i++) {
      if (result.results[i].characters.includes(wedge)) {
        count++;
      }
    }
    console.log(count);
  }
});
