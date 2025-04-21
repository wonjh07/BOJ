let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let N = +input[0];
let k = +input[1];

const calc = (x) => {
  let temp = 0;

  for (let i = 1; i <= N; i++) {
    temp += Math.min(Math.floor(x / i), N);
  }

  return temp;
};

let [left, right] = [1, k];
while (left < right) {
  let mid = (left + right) >> 1;
  if (calc(mid) < k) {
    left = mid + 1;
  } else right = mid;
}

console.log(left);

process.exit();
