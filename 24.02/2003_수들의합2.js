const [NM, input] = require("fs")
  .readFileSync("input.txt") //  '/dev/stdin'
  .toString()
  .trim()
  .split("\n");

const [N, M] = NM.split(" ").map(Number);
const arr = input.split(" ").map(Number);

let answer = 0;
let total = 0;
let pointer = 0;

for (let i = 0; i < N; i++) {
  total += arr[i];
  if (total < M) continue;
  while (total > M && pointer <= i) {
    total -= arr[pointer];
    pointer += 1;
  }
  if (total === M) answer += 1;
}

console.log(answer);
process.exit();
