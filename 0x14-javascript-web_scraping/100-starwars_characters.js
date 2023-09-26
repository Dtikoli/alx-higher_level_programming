#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, content) => {
  if (!err) {
    const characters = JSON.parse(content).characters;
    characters.forEach(character => {
      request(character, (error, resp, content) => {
        if (!error) {
          const name = JSON.parse(content).name;
          console.log(name);
        }
      });
    });
  }
});
