#!/usr/bin/node
exports.esrever = function (list) {
  const listReverse = [];
  list.forEach(element => listReverse.unshift(element));
  return listReverse;
};
