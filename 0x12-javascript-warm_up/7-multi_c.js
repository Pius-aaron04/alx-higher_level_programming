#!/usr/bin/node
const { argv } = require('process');
const numberOfOcc = Number(argv[2]);
if (isNaN(numberOfOcc)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberOfOcc; i++) {
    console.log('C is fun');
  }
}
