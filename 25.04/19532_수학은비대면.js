let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [a, b, c, d, e, f] = input[0].split(" ").map(Number);

const x = (c * e - b * f) / (a * e - b * d);
const y = (c * d - a * f) / (b * d - a * e);

console.log([Math.round(x), Math.round(y)].join(" "));

process.exit();

// console.log(Math.round(x), Math.round(y));
// .join(" ") 을 해주지않으면 공백의 유무로 에러가 날 수 있음
// 이유는 잘 모르겠다
