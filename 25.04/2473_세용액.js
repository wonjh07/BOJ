let input = require("fs")
  .readFileSync("./input.txt") // .readFileSync(0)
  .toString()
  .trim()
  .split("\n");

function main() {
  let N = +input[0];
  let flasks = input[1]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  let ans = [];
  let cnt = Infinity;

  for (let i = 0; i < N - 2; i++) {
    let [left, right] = [i + 1, N - 1];
    const a = flasks[i];

    while (left < right) {
      const b = flasks[left];
      const c = flasks[right];
      const sum = a + b + c;
      const absSum = Math.abs(sum);
      if (cnt > absSum) {
        cnt = absSum;
        ans = [a, b, c];
      }
      if (sum < 0) left++;
      else right--;
    }
  }

  console.log(ans.join(" "));
  process.exit();
}

main();

// 이전코드
// 구조분해, 이중반복 + 이분탐색으로 비효율적인 코드
// let input = require("fs")
//   .readFileSync("./input.txt") // .readFileSync(0)
//   .toString()
//   .trim()
//   .split("\n");

// function main() {
//   let N = +input[0];
//   let flasks = input[1]
//     .split(" ")
//     .map(Number)
//     .sort((a, b) => a - b);
//   let ans = [];
//   let cnt = Infinity;

//   function bs(i, j, target) {
//     let [st, ed] = [i + 1, j - 1];

//     while (st < ed) {
//       const mid = (st + ed) >> 1;
//       if (flasks[mid] <= target) st = mid + 1;
//       else ed = mid;
//     }
//     if (
//       st - 1 > i &&
//       Math.abs(target - flasks[st - 1]) < Math.abs(target - flasks[st])
//     ) {
//       return st - 1;
//     }
//     return st;
//   }

//   for (let i = 0; i < N; i++) {
//     for (let j = N - 1; j > i + 1; j--) {
//       let now = flasks[i] + flasks[j];
//       const target = -now;
//       const middle = bs(i, j, target);
//       now += flasks[middle];
//       if (cnt > Math.abs(now)) {
//         cnt = Math.abs(now);
//         ans = [i, middle, j];
//       }
//     }
//   }

//   ans = ans.map((e) => flasks[e]);
//   console.log(ans.join(" "));

//   process.exit();
// }

// main();

/*
N 3 ~ 5000
세가지 용액을 골라 가장 0에 가깝게 만들어라
용액을 오름차순으로 출력
용액들의 값은 중복 되지 않음
-1,000,000,000 ~ 1,000,000,000 10억
두개 이상일 경우에는 아무거나 하나 출력 - 먼저 찾은거 뱉고 종료

가장 원초적인 dfs() 최대 100만 루프
일단 오름차순 정렬
왼쪽끝 오른쪽끝 투포인터로 두가지 고르고
0에 최대한 가까워지는 값 이분탐색

+가 많을때는 최대한 왼쪽으로 쏠림
-가 많을때는 오른쪽으로 쏠림
*/

/*
1등코드
const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").toString().trim().split("\n");

const N = Number(input[0]);
const solutions = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
let min = Infinity;
let result = [0, 0, 0];

for (let i = 0; i < N - 2; i++) {
  const a = solutions[i];
  let front = i + 1;
  let rear = N - 1;

  while (front < rear) {
    const b = solutions[front];
    const c = solutions[rear];
    const sum = a + b + c;

    if (Math.abs(sum) < min) {
      min = Math.abs(sum);
      result = [a, b, c];
    }

    if (sum > 0) rear--;
    else front++;
  }
}

console.log(result.join(" "));
*/
