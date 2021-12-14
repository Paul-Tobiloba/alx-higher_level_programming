#!/usr/bin/node
function add (a, b) {
  if (a && b) {
    return (a + b);
  }
  return NaN;
}

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
