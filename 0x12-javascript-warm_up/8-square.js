#!/usr/bin/node
/*
 * A script that prints a square
 */

const process = require('process');
const args = process.argv;
const myNum = parseInt(args[2]);
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('X'.repeat(myNum));
  }
}
