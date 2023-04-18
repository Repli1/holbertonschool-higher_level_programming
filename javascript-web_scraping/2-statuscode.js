#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
  console.log('code: ' + response.statusCode);
});
