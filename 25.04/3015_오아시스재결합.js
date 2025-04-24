let input = require("fs")
  .readFileSync("./input.txt") // .readFileSync(0)
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const N = input[0];
const stack = [];
const cnt = [];
let ans = 0;

for (let i = 1; i <= N; i++) {
  const now = +input[i];
  let cntNow = 1;

  while (stack.length && stack[stack.length - 1] <= now) {
    const lastIdx = stack.length - 1;
    if (stack[lastIdx] === now) cntNow += cnt[lastIdx];
    ans += cnt[lastIdx];
    stack.pop();
    cnt.pop();
  }

  if (stack.length) ans += 1;
  stack.push(now);
  cnt.push(cntNow);
}

console.log(ans);

// 이전코드
// let fs = require("fs");
// let input = fs
//   .readFileSync("./input.txt") // .readFileSync(0)
//   .toString()
//   .trim()
//   .split("\n")
//   .map(Number);

// const N = input[0];
// const stack = [];
// let ans = 0;

// for (let i = 1; i <= N; i++) {
//   const now = +input[i];
//   let cnt = 1;

//   while (stack.length && stack[stack.length - 1][0] <= now) {
//     if (stack[stack.length - 1][0] === now) cnt += stack[stack.length - 1][1];
//     ans += stack[stack.length - 1][1];
//     stack.pop();
//   }

//   if (stack.length) ans += 1;
//   stack.push([now, cnt]);
// }

// console.log(ans);

/*
1등 코드

const input = require('fs').readFileSync(0).toString().trim().split('\n').map(Number);

const N = input.shift();
const stack = [];
const counts = [];

let answer = 0;

input.forEach((person) => {
  let sameCount = 1;

  while (stack.length && stack[stack.length - 1] <= person) {
    answer += counts[counts.length - 1];

    if (stack[stack.length - 1] === person) {
      sameCount = counts[counts.length - 1] + 1;
    }

    stack.pop();
    counts.pop();
  }

  if (stack.length > 0) {
    answer += 1;
  }

  stack.push(person);
  counts.push(sameCount);
});

console.log(answer);
*/
