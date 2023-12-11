#!/usr/bin/node

// This script prints a message depending of the number of arguments passed:

if (process.argv.length === 2) {
  console.log('No argument');
}
if (process.argv.length === 3) {
  console.log('Argument found');
}
if (process.argv.length > 3) {
  console.log('Arguments found');
}
