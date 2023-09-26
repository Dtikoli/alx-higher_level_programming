#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, content) => {
  const resp = {};
  const task = JSON.parse(content);
  for (let i = 0; i < task.length; i++) {
    if (task[i].completed) {
      if (resp[task[i].userId] === undefined) {
        resp[task[i].userId] = 0;
      }
      resp[task[i].userId]++;
    }
  }
  console.log(error || resp);
});
