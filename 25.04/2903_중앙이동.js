let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let T = +input;
ans = 2;
for (let i = 0; i < T; i++) {
  ans += ans - 1;
}
console.log(ans ** 2);
process.exit();

/*
1등코드

var a = { '0': 2 };
for(var i = 1; i <= 15; ++i) {
  a[i] = a[i - 1] + (a[i - 1] - 1);
}
console.log(Math.pow(a[require('fs').readFileSync('/dev/stdin').toString().trim()], 2));

*/
