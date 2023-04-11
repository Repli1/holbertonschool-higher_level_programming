#!/usr/bin/node
const process = require('process');
const args = process.argv;
if (isNaN(args[2]) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    console.log('X'.repeat(parseInt(args[2])));
  }
}
