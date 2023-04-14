#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const args2 = args.slice(2, args.length + 1);
  args2.sort(function (a, b) {
    return a - b;
  });
  console.log(args2[args2.length - 2]);
}
