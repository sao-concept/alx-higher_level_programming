#!/usr/bin/node

// This script prints x times “C is fun”.

const myArg = process.argv[2];

if (isNaN(Number(myArg))) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < myArg; i++) {
    console.log('C is fun');
  }
}
