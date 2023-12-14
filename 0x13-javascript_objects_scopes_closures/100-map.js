#!/usr/bin/node
const data = require('./100-data').list;

const newArray = data.map((x, index) => x * index);

console.log(data);
console.log(newArray);
