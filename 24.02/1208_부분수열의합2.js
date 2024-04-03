const [[N, S], input] = require("fs")
  .readFileSync("input.txt") // '/dev/stdin'
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

const dict = new Map();
const middle = Math.round(N / 2);
const arr1 = input.slice(0, middle);
const arr2 = input.slice(middle, N);
let ans = 0;

const combination1 = (i, sum) => {
  if (i === arr1.length) {
    dict.has(sum) ? dict.set(sum, dict.get(sum) + 1) : dict.set(sum, 1);
    return;
  }
  combination1(i + 1, sum + arr1[i]);
  combination1(i + 1, sum);
};

const combination2 = (i, sum) => {
  if (i === arr2.length) {
    if (dict.has(S - sum)) ans += dict.get(S - sum);
    return;
  }
  combination2(i + 1, sum + arr2[i]);
  combination2(i + 1, sum);
};

combination1(0, 0);
combination2(0, 0);

console.log(ans);
process.exit();

/*
1등코드

let func1 = (k, sum) => {
  if (k === part1.length) {
    sumSet.has(sum) ? sumSet.set(sum, sumSet.get(sum) + 1) : sumSet.set(sum, 1);
    return;
  }

  func1(k + 1, sum);
  func1(k + 1, sum + part1[k]);
};

let func2 = (k, sum) => {
  if (k === part2.length) {
    if (sumSet.has(s - sum)) ans += sumSet.get(s - sum);
    return;
  }

  func2(k + 1, sum);
  func2(k + 1, sum + part2[k]);
};

const [[n, s], arr] = (require('fs').readFileSync('/dev/stdin') + '')
  .trim()
  .split(/\r?\n/)
  .map((v) => v.split(' ').map((v) => +v));

let ans = 0;
const part1 = arr.slice(0, Math.floor(n / 2));
const part2 = arr.slice(Math.floor(n / 2));
const sumSet = new Map();
func1(0, 0);
func2(0, 0);
if (s === 0) ans--;
console.log(ans);

*/
