let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let N = +input[0];
let nums = input[1].split(" ").map(Number);
let lis = [0];

const binSearch = (num) => {
  let [left, right] = [0, lis.length];
  while (left < right) {
    let mid = (left + right) >> 1;
    if (lis[mid] < num) left = mid + 1;
    else right = mid;
  }

  if (left === lis.length) lis.push(num);
  else lis[left] = num;
};

for (let num of nums) {
  binSearch(num);
}

console.log(lis.length);

process.exit();

/* 1등 코드
let input = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(e => e.split(' ').map(Number));
const stack = []
stack[0]=0;
const list=input[1]
list.forEach(c => {
    
      let left = 0;
      let right = stack.length;
      while (left + 1 < right) {
        const mid = (left + right) >> 1;
        if (stack[mid] < c) left = mid;
        else right = mid;
      }
      stack[right] = c;
    
  });
console.log(stack.length-1);
*/
