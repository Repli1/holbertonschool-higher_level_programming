#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let sorted = args.slice(2, args.length + 1);
  sorted.sort();
  console.log(sorted[sorted.length - 2]);
}
