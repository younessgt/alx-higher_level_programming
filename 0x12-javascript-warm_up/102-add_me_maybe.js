#!/usr/bin/node
exports.addMeMaybe = function (x, theFunction) {
  const nb = x + 1;
  theFunction(nb);
};
