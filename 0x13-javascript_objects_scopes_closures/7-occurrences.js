#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const reducer = (accumulator, currentValue) => accumulator + (currentValue === searchElement);
  return list.reduce(reducer, 0);
};
