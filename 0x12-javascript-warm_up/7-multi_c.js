#!/usr/bin/node

const myVar = 'C is fun';
const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(myVar);
  }
}
