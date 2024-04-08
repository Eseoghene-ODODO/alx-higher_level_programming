#!/usr/bin/node

/**
 * A function that increments and calls a function
 * The function must be visible from outside
 * Prototype: function (number, theFunction)
 */

function addMeMaybe (number, theFunction) {
  number++;
  theFunction(number);
}
exports.addMeMaybe = addMeMaybe;
