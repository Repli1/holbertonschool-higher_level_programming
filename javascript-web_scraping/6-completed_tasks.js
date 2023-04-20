#!/usr/bin/node
const request = require('request');
const args = process.argv;
const url = args[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const result = JSON.parse(body);
    for (let i = 0; result[i] !== undefined; i++) {
      if (result[i].completed === true) {
        if (result[i].userId in dict) {
          dict[result[i].userId] += 1;
        } else {
          dict[result[i].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
