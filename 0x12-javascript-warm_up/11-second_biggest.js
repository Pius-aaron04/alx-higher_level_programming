#!/usr/bin/node
const { argv } = require('process');
const numbers = [];
let i = 0;
while (argv[i + 2]) {
  numbers[i] = argv[i + 2];
  i++;
}

if (numbers.length === 1 || numbers.length === 0) {
  console.log('0');
} else {
  numbers.sort();
  numbers.reverse();
  console.log(numbers[1]);
}
