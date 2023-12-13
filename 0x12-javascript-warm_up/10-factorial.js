#!/usr/bin/node
// finds the factorial of number passed as argument
const { argv } = require('process');
const number = Number(argv[2]);

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(number));
