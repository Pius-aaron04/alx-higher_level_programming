#!/usr/bin/node
const { argv } = require('process');
const argument = Number(argv[2]);

if (!isNaN(argument)) {
  console.log(`My number ${argument}`);
} else {
  console.log('Not a number');
}
