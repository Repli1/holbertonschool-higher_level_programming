#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv;
request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = body;
    fs.writeFile(args[3], result, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
