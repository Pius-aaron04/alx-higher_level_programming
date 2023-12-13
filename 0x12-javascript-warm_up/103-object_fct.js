#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
function increment () {
  myObject.value += 1;
}
myObject.incr = Object.assign(function () {}, increment);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
