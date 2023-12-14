#!/usr/bin/node

let callCounter = 0;

exports.logMe = function (item) {
  console.log(`${callCounter}: ${item}`);
  callCounter++;
};
