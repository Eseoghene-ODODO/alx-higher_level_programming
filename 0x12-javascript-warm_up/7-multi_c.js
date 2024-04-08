#!/usr/bin/node
/*
 * A script that prints x times “C is fun”
 */

const process = require('process');
const args = process.argv;
const myNum = parseInt(args[2]);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNum; i++) {
    console.log('C is fun');
  }
}
