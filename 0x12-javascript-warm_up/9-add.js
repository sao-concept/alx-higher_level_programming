#!/usr/bin/node

// This script prints the addition of 2 integers

function add (a, b) {
  return (a + b);
}

if (isNaN(Number(process.argv[2])) || isNaN(Number(process.argv[3]))) {
  console.log('NaN');
} else {
  console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
}
