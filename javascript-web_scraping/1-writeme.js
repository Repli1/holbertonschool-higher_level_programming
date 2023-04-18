#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const data = args[3];
fs.writeFile(args[2], data, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
