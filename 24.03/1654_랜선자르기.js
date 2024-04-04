const input = require("fs")
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [K, N] = input[0].split(" ").map(Number);
const lans = input.splice(1).map(Number);

let start = 1;
let end = Math.max(...lans);
let answer = 0;

while (start <= end) {
  let middle = parseInt((start + end) / 2);
  let tmp = 0;
  for (let i of lans) {
    tmp += parseInt(i / middle);
  }

  if (tmp >= N && middle > answer) answer = middle;

  if (tmp < N) end = middle - 1;
  else if (tmp >= N) start = middle + 1;
}

console.log(answer);
process.exit();