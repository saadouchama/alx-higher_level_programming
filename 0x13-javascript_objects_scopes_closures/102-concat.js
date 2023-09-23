#!/usr/bin/node
const fs = require('fs');
const file1 = fs.readFileSync(process.argv[2], 'utf8');
const file2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], file1 + file2);
