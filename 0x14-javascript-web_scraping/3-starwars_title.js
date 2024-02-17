#!/usr/bin/node

/*
 * loads data from Star Wars API
 */
const request = require('request');
const { argv } = require('process');

request.get(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (body) {
    // loads json data
    console.log(JSON.parse(body).title);
  }
});
