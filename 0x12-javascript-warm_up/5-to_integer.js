#!/usr/bin/node
/*
 * A script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
 */

const process = require('process');
const args = process.argv;
if (args[2] === undefined) {
  console.log('Not a number');
} else {
  console.log(parseInt(args[2]));
}
