#!/usr/bin/node
function callMeMoby (x, theFunction) {
  while (x > 0) {
    x--;
    theFunction();
  }
}

module.exports = { callMeMoby };
