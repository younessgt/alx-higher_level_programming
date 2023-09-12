#!/usr/bin/node
const fs = require('fs');
const arg = process.argv.slice(2);
const contFile1 = fs.readFileSync(arg[0], 'utf8');
const contFile2 = fs.readFileSync(arg[1], 'utf8');
const contFile3 = contFile1 + contFile2;
fs.writeFileSync(arg[2], contFile3);
