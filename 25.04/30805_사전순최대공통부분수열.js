let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = +input[0];
let arrN = input[1].split(" ").map(Number);
const M = +input[2];
let arrM = input[3].split(" ").map(Number);

const mx = Math.max(Math.max(...arrN), Math.max(...arrM));
let ans = [];

for (let i = mx; i > 0; i--) {
  while (1) {
    if (!arrN.includes(i) || !arrM.includes(i)) break;
    ans.push(i);
    arrN = arrN.slice(arrN.indexOf(i) + 1);
    arrM = arrM.slice(arrM.indexOf(i) + 1);
  }
}

console.log(ans.length);
console.log(ans.join(" "));
