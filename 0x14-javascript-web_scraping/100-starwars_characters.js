#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(url, (err, response, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, (error, resp, body) => {
        if (!error) {
          const name = JSON.parse(body).name;
          console.log(name);
        }
      });
    });
  }
});
