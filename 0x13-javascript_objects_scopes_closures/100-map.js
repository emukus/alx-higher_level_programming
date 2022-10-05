#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const listed = list.map((index, elem) => index * elem);
console.log(listed);
