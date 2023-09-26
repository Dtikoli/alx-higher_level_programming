#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, content) => {
  if (error) {
    console.log(error);
    return;
  }

  const taskCompleted = {};
  const todoList = JSON.parse(content);
  for (const task of todoList) {
    if (task.completed) {
      if (!taskCompleted[task.userId]) {
        taskCompleted[task.userId] = 0;
      }
      taskCompleted[task.userId]++;
    }
  }
  console.log(taskCompleted);
});
