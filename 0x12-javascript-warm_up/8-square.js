#!/usr/bin/node

// This script prints a square.

const myArg = process.argv[2];
let rows = 'X';

if (isNaN(Number(myArg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArg - 1; i++) {
    rows += 'X';
  }
  for (let j = 0; j < myArg; j++) {
    console.log(rows);
  }
}
