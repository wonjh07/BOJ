let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let result = 0;

const checkNum = (x) => {
  if (["Fizz", "Buzz", "FizzBuzz"].includes(x)) return false;
  else return true;
};

for (let i = 0; i < 3; i++) {
  if (checkNum(input[i])) {
    result = Number(input[i]) + (3 - i);
    break;
  }
}

if (result % 3 === 0 && result % 5 === 0) console.log("FizzBuzz");
else if (result % 3 === 0 && result % 5 !== 0) console.log("Fizz");
else if (result % 3 !== 0 && result % 5 === 0) console.log("Buzz");
else console.log(result);

process.exit();
