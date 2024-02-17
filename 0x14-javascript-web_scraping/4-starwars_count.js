#!/usr/bin/node

/*
 * Manipulates data from API
 */

const request = require('request');
const { argv } = require('process');

request.get(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (body) {
    const films = JSON.parse(body).results;
    let count = 0;
    films.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes('18')) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
