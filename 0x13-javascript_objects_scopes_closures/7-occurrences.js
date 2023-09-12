#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const elem of list) {
    if (elem === searchElement) {
      counter++;
    }
  }
  return counter;
};
/* we can use also the reduce method
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((counter, elem) => { return counter === elem ? counter + 1 : counter }, 0);
};
*/
