#!/usr/bin/node

/*
 * Writes to file passed as argument
 * Usage: ./1-writeme.js <file_path> <string>
 */

const { argv } = require('process');
const fs = require('node:fs');

fs.writeFile(argv[2], argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});
