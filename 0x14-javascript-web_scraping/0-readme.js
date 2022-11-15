#!/usr/bin/node
// Reads and prints the content of a file
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, data) {
  console.log(error || data);
});
