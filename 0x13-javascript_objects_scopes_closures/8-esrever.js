#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length - 1;
  const revList = [];

  for (let i = len; i >= 0; i--) {
    revList.push(list[i]);
  }

  return (revList);
};
