#!/usr/bin/node

const request = require('request');
const matchId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${matchId}`;

request(url, (error, response, content) => {
  console.log(error || JSON.parse(content).title);
});
