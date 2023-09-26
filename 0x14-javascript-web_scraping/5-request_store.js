#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fileStream = fs.createWriteStream(file);

fileStream.on('error', (error) => {
  console.error(error);
});

request(url).pipe(fileStream);
