#!/usr/bin/node
/*
 * A script that prints first argument passed to it..
 */

const process = require('process');
const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
