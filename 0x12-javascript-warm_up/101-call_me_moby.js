#!/usr/bin/node

function callMeMoby (x, theFunction) {
  while (x) {
    x--;
    theFunction();
  }
}

module.exports = { callMeMoby };
