#!/usr/bin/node

/*
 * Writes the content to a web page to a file
 * Usage: 5-request_store.js <url> <file_path>
 */

const { argv } = require('process');
const fs = require('node:fs');
const request = require('request');

request.get(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    // writes to the file passed
    fs.writeFile(argv[3], body, (error) => {
      if (error) console.error(error);
    });
  }
});
