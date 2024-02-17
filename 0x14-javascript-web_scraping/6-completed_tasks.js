#!/usr/bin/node

/*
 * prints users with completed tasks data
 * Usage: ./6-completed_tasks.js <uri>
 * example: ./6-completed-task.js https://jsonplaceholder.typicode.com/todos
 * {
 *     1: 11,
 *     2, 3,
 *     ...
 * }
 */

const { argv } = require('process');
const request = require('request');

request.get(argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const usersTasks = {};
    tasks.forEach((task) => {
      if (!(task.userId in usersTasks) && task.completed) {
        usersTasks[task.userId] = 1;
      } else if ((task.userId in usersTasks) && task.completed) {
        usersTasks[task.userId] += 1;
      }
    });
    console.log(usersTasks);
  }
});
