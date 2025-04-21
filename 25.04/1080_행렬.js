// 비공식 1등 달성

const main = () => {
  let fs = require("fs");

  let input = fs
    .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
    .toString()
    .trim()
    .split("\n");

  let [N, M] = input.shift().split(" ").map(Number);
  let arr = new Array(N).fill().map(() => new Array(M).fill(0));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (input[i][j] != input[i + N][j]) arr[i][j] = 1;
      else arr[i][j] = 0;
    }
  }

  let ans = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (arr[i][j] === 0) continue;
      else {
        if (i >= N - 2 || j >= M - 2) return console.log(-1);

        for (let di = 0; di <= 2; di++) {
          for (let dj = 0; dj <= 2; dj++) {
            arr[i + di][j + dj] = arr[i + di][j + dj] === 1 ? 0 : 1;
          }
        }
        ans += 1;
      }
    }
  }
  console.log(ans);
  return;
};

main();

process.exit();
