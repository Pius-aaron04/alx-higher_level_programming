#!/usr/bin/node
// finds the factorial of number passed as argument
const { argv } = require('process');
const number = Number(argv[2]);

function factorial (num) {
  if (isNaN(number) || number === 0) {
    console.log('1');
  } else {
    let factorial = 1;
    for (num; num !== 1; num--) {
      factorial *= num;
    }
    console.log(factorial);
  }
}

factorial(number);
