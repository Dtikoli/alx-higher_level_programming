#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nOccur = 0;
  let i = 0;

  while (i < list.length) {
    if (searchElement === list[i]) {
      nOccur++;
    }
    i++;
  }
  return nOccur;
};
