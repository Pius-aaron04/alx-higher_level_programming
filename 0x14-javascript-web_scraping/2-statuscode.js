#!/usr/bin/node

/**
 * gets the status of a url
 */

const { argv } = require('node:process');
const request = require('request');

request.get(argv[2], (err, response, body) => {
  console.log('code:', response && response.statusCode);
  if (err) {
    console.log(err);
  }
});
