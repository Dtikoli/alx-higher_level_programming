#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, content) => {
  if (!error) {
    const characters = JSON.parse(content).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, content) => {
    if (!error) {
      console.log(JSON.parse(content).name);
      printCharacters(characters, index + 1);
    }
  });
}
