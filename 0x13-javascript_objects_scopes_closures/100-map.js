#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const newList = list.map((index, elem) => index * elem);
console.log(newList);
