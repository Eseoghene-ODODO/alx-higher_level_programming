#!/usr/bin/node
/*
 * A script that prints the addition of 2 integers
 */

function add (a, b) {
  return a + b;
}
const process = require('process');
const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);
if ((isNaN(num1) || isNaN(num2)) && (num1 === undefined || num2 === undefined)) {
  console.log(NaN);
} else {
  console.log(add(num1, num2));
}
