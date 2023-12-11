#!/usr/bin/node

/*
 This script prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
*/

const myArg = process.argv[2];

if (isNaN(Number(myArg))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArg);
}
