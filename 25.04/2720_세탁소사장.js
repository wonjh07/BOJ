let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let T = +input.shift();
input = input.map(Number);

const calc = (m) => {
  let ans = [0, 0, 0, 0];

  ans[0] = Math.floor(m / 25);
  m %= 25;

  ans[1] = Math.floor(m / 10);
  m %= 10;

  ans[2] = Math.floor(m / 5);
  m %= 5;

  ans[3] = m;

  return ans.join(" ");
};

input.forEach((i) => console.log(calc(i)));

process.exit();

/*
2등 코드

const input = require("fs").readFileSync("/dev/stdin").toString().split("\n").map(Number);
const n = input[0];
let arr = [25,10,5,1];
let answer = "";

for(i=1; i<=n; i++){
  for(j=0;j<4;j++){
    answer += Math.floor(input[i]/arr[j]) + " ";
    input[i] = input[i]%arr[j];
  }
}
console.log(answer);

*/
