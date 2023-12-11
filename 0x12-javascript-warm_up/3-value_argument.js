#!/usr/bin/node

/*
 This script prints the first argument passed to it:

 If no arguments are passed to the script, print “No argument”
 It use console.log(...) to print all output
 Not allowed to use var
 Not allowed to use length
*/

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
