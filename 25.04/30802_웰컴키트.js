// 1등 코드
let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = Number(input[0]);
const size = input[1].split(" ").map(Number);
const [T, P] = input[2].split(" ").map(Number);

let cnt = 0;

const calc = (ea) => {
  if (ea === 0) return 0;

  if (ea <= T) return 1;
  let rst = Math.floor(ea / T);

  if (ea % T) rst += 1;
  return rst;
};

size.forEach((x) => (cnt += calc(x)));

console.log(cnt);
console.log(Math.floor(N / P), N % P);

process.exit();
