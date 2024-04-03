// 백준 1등코드 달성

let input = require("fs")
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const T = +input[0];
const K = +input[T + 1];
const spins = input.splice(-K).map((_) => _.split(" "));
const gearWheels = input.splice(1, T).map((_) => _.split(""));
const eachSpin = new Array(T).fill(0);
let answer = 0;

const rightSpin = (num, direct) => {
  if (num > 0 && direct !== 1) {
    const leftOne = gearWheels[num - 1].at((2 + eachSpin[num - 1]) % 8);
    const thisOne = gearWheels[num].at((6 + eachSpin[num]) % 8);
    if (leftOne !== thisOne) leftSpin(num - 1, -1);
  }
  if (num < T - 1 && direct !== -1) {
    const rightOne = gearWheels[num + 1].at((6 + eachSpin[num + 1]) % 8);
    const thisOne = gearWheels[num].at((2 + eachSpin[num]) % 8);
    if (rightOne !== thisOne) leftSpin(num + 1, 1);
  }
  eachSpin[num] -= 1;
};

const leftSpin = (num, direct) => {
  if (num > 0 && direct !== 1) {
    const leftOne = gearWheels[num - 1].at((2 + eachSpin[num - 1]) % 8);
    const thisOne = gearWheels[num].at((6 + eachSpin[num]) % 8);
    if (leftOne !== thisOne) rightSpin(num - 1, -1);
  }
  if (num < T - 1 && direct !== -1) {
    const rightOne = gearWheels[num + 1].at((6 + eachSpin[num + 1]) % 8);
    const thisOne = gearWheels[num].at((2 + eachSpin[num]) % 8);
    if (rightOne !== thisOne) rightSpin(num + 1, 1);
  }
  eachSpin[num] += 1;
};

for (let [n, d] of spins) {
  if (d === "1") rightSpin(n - 1, 0);
  else leftSpin(n - 1, 0);
}

eachSpin.forEach((e, idx) => {
  if (gearWheels[idx].at(e % 8) === "1") answer += 1;
});

console.log(answer);
process.exit();
