#!/usr/bin/node
// This function adds two numbers passed at the commnad line

const { argv } = require('process');

function add (num1, num2) {
  console.log(num1 + num2);
}

add(Number(argv[2]), Number(argv[3]));
