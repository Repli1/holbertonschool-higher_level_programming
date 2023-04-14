#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let biggest = parseInt(args[2]);
  let second = parseInt(args[3]);
  for (let i = 3; i < args.length; i++) {
    if (parseInt(args[i]) >= biggest) {
      second = biggest;
      biggest = parseInt(args[i]);
    }
  }
  console.log(second);
  console.log(biggest);
}
