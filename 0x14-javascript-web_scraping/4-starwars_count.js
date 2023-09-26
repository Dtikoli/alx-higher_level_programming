#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, content) => {
  const results = JSON.parse(content).results;
  const num = results.reduce((count, film) => {
    return film.characters.find((character) => character.endsWith('/18/'))
      ? count + 1
      : count;
  }, 0);
  console.log(error || num);
});
