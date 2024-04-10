#!/usr/bin/node

/**
 * A script that concats 2 files
 * The first argument is the file path of the first source file
 * The second argument is the file path of the second source file
 * The third argument is the file path of the destination
 */

const fs = require('fs');

const [sourceFile1, sourceFile2, destinationFile] = process.argv.slice(2);

const data1 = fs.readFileSync(sourceFile1, 'utf8');
const data2 = fs.readFileSync(sourceFile2, 'utf8');

fs.writeFileSync(destinationFile, data1 + data2);
