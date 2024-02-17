#!/usr/bin/node

/*
 * Displays all chracters that played in the Star Wars movie
 * specified with the ID
 * Usage: ./100-starwars_characters.js <movieID>
 */

const { argv } = require('process');
const request = require('request');

request.get(`https://swapi-api.alx-tools.com/api/films/${argv[2]}/`, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request.get(character, (error, resp, data) => {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(data).name);
        }
      });
    });
  }
});
