#!/usr/bin/node

/*
 * This script read and writes to stdout the content of the file
 * passed as argument
 */

const fs = require('node:fs');
const { argv } = require('process');

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else if (data) {
    console.log(data);
  }
});
