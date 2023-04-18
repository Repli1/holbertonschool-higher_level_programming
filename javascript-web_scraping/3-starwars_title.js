#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = 'https://swapi.dev/api/films/'
request(url + args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);
    console.log(result.title);
  }
});
