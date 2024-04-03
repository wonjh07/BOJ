let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n");
// let input = fs.readFileSync("/dev/stdin").toString();

// 자연수 A의 약수의 합 = f(A)
// x보다 작거나 같은 모든 자연수 y의 f(y) 값을 더한 값은 g(x)

let ans = 0;

const getDivisors = (num) => {
  let temp = +num + 1;

  for (let i = 2; i < num; i++) {
    let div = i;
    while (num > 1) {
      if (num % div === 0) {
        temp += div;
        div = div ** 2;
      } else {
        break;
      }
    }
  }

  return temp;
};

console.log(getDivisors(input));
