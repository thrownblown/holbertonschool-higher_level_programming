#!/usr/bin/node
let fact = process.argv[2];

let factorial = (a) => {
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
};

if (isNaN(fact)) {
  console.log(1);
} else {
  console.log(factorial(fact));
}
