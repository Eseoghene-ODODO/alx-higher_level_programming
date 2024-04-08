#!/usr/bin/node
/*
 * A script that prints two arguments passed to it in the following formart: "is"
 */

const process = require('process');
const args = process.argv;
console.log(args[2] + ' is ' + args[3]);
