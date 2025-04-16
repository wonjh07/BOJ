// 1등 코드 달성
let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = +input[0];
const fruits = input[1].split(" ").map(Number);
let check = new Array(10).fill(0);
let ans = 2;
let cnt = 0;

if (N <= 2) console.log(N);
else {
  let [st, end] = [0, 1];
  let len = 2;
  check[fruits[0]] += 1;
  check[fruits[1]] += 1;

  if (fruits[0] === fruits[1]) cnt = 1;
  else cnt = 2;

  while (end < N - 1) {
    end += 1;
    if (check[fruits[end]] === 0) cnt += 1; 
    check[fruits[end]] += 1;
    len += 1;

    if (end === N - 1 && cnt > 2) break;
    while (cnt > 2) {
      check[fruits[st]] -= 1;
      if (check[fruits[st]] === 0) cnt -= 1;
      len -= 1;
      st += 1;
    }
    if (ans < len) ans = len;
  }

  console.log(ans);
}

process.exit();
