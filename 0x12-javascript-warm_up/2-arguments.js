#!/usr/bin/node
/*
 * A script that prints a message depending on yhe number  of arguments passed.
 */

const process = require('process');
const args = process.argv;
if (args.length <= 2) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
