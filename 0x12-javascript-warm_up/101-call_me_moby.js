#!/usr/bin/node

/**
 * A function that executes x times a function.
 * The function must be visible from outside
 * Prototype: function (x, theFunction)
 */

function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}
exports.callMeMoby = callMeMoby;
