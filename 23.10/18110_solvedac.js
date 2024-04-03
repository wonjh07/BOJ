let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n").map(Number);
// let input = fs.readFileSync('/dev/stdin').toString().split('\n').map(Number);

const main = () => {
  const N = input.shift();
  const TN = Math.round(N * 0.15);
  const sum = input
    .sort((a, b) => a - b)
    .slice(TN, N - TN)
    .reduce((tot, now) => tot + now, 0);
  return Math.round(sum / (N - 2 * TN)) || 0;
};

console.log(main());

/*
배운점

shift()가 splice(), slice() 보다 빠르다.

sort((a, b) => a - b) : 오름차순 ASC
sort((a, b) => a + b) : 내림차순 DESC

return Math.round(sum / (N - 2 * TN)) || 0;
이구문에서 결과값이 NaN이면 || 에 의해서 0 으로 return

*/
