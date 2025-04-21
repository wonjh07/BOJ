// 1등코드
let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [N, C] = input[0].split(" ").map(Number);
let sack = input[1].split(" ").map(Number);
const mid = Math.round(sack.length / 2) - 1;
let [st1, ed1] = [0, mid];
let [st2, ed2] = [mid + 1, sack.length];
let ans = 0;

let stk1 = [0];
let stk2 = [0];

const dfs1 = (now, i) => {
  if (i > ed1) return;
  let temp = now + sack[i];
  if (temp <= C) {
    stk1.push(temp);
    dfs1(temp, i + 1);
  }
  dfs1(now, i + 1);
};

const dfs2 = (now, i) => {
  if (i > ed2) return;
  let temp = now + sack[i];
  if (temp <= C) {
    stk2.push(temp);
    dfs2(temp, i + 1);
  }
  dfs2(now, i + 1);
};

dfs1(0, st1);
dfs2(0, st2);

stk2.sort((a, b) => a - b);

const binarySearch = (i) => {
  let start = 0;
  let end = stk2.length;
  let target = C - i;
  while (start < end) {
    let middle = Math.floor((start + end) / 2);
    if (stk2[middle] <= target) start = middle + 1;
    else end = middle;
  }

  return start;
};

for (i of stk1) {
  ans += binarySearch(i);
}

console.log(ans);

process.exit();
