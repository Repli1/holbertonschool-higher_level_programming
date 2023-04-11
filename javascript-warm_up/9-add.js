#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (isNaN(args[2]) === true || isNaN(args[3]) === true) {
  console.log('NaN');
} else {
  function add (a, b) {
    return (parseInt(a) + parseInt(b));
  }
  console.log(add(args[2], args[3]));
}
