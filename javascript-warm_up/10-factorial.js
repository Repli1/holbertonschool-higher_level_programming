#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (isNaN(args[2]) === true) {
  console.log(1);
} else {
  function factorial (a) {
    if (a === 1) {
      return (1);
    } else {
      return (a * factorial(a - 1));
    }
  }
  console.log(factorial(parseInt(args[2])));
}
