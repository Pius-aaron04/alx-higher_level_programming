#!/usr/bin/node

/*
 * Manipulates data from API
 */

const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/films/', (err, response, body) => {
  if (err) {
    console.log(err);
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
