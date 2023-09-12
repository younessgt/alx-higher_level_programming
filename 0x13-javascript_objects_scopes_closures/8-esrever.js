#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  let len = list.length - 1;
  while (len > 0 && len > i) {
    const temp = list[len];
    list[len] = list[i];
    list[i] = temp;
    len--;
    i++;
  }
  return list;
};
