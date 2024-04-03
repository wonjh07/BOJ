let [[N, M, R], ...input] = require("fs")
  .readFileSync("input.txt") // '/dev/stdin'
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

const orders = input.pop();
// 1: 상하반전, 2: 좌우반전, 3:오른쪽90도회전, 4: 왼쪽90도회전
// 5: 1-> 2-> 3 -> 4->1, 6: 1-> 4 -> 3 -> 2 -> 1

for (let order of orders) {
  //1
  if (order === 1) {
    for (let j = 0; j < M; j++) {
      for (let i = 0; i < N / 2; i++) {
        [input[i][j], input[N - i - 1][j]] = [input[N - i - 1][j], input[i][j]];
      }
    }
  }

  //2
  if (order === 2) {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M / 2; j++) {
        [input[i][j], input[i][M - j - 1]] = [input[i][M - j - 1], input[i][j]];
      }
    }
  }

  //3
  if (order === 3) {
    const visit = new Array(M).fill().map((_, i) => new Array(N).fill(0));
    for (let j = 0; j < M; j++) {
      for (let i = 0; i < N; i++) {
        visit[j][N - 1 - i] = input[i][j];
      }
    }
    input = [...visit];
    [N, M] = [M, N];
  }

  //4
  if (order === 4) {
    const visit = new Array(M).fill().map((_, i) => new Array(N).fill(0));
    for (let j = 0; j < M; j++) {
      for (let i = 0; i < N; i++) {
        visit[j][i] = input[i][M - j - 1];
      }
    }
    input = [...visit];
    [N, M] = [M, N];
  }

  //5
  if (order === 5) {
    const visit = new Array(N).fill().map((_, i) => new Array(M).fill(0));
    const nh = Math.round(N / 2, 0);
    const mh = Math.round(M / 2, 0);
    const dy = [0, 0, nh, nh, 0];
    const dx = [0, mh, mh, 0, 0];

    for (let d = 0; d < 4; d++) {
      for (let i = 0; i < nh; i++) {
        for (let j = 0; j < mh; j++) {
          visit[i + dy[d + 1]][j + dx[d + 1]] = input[i + dy[d]][j + dx[d]];
        }
      }
    }
    input = [...visit];
  }

  //6
  if (order === 6) {
    const visit = new Array(N).fill().map((_, i) => new Array(M).fill(0));
    const nh = Math.round(N / 2, 0);
    const mh = Math.round(M / 2, 0);
    const dy = [0, nh, nh, 0, 0];
    const dx = [0, 0, mh, mh, 0];

    for (let d = 0; d < 4; d++) {
      for (let i = 0; i < nh; i++) {
        for (let j = 0; j < mh; j++) {
          visit[i + dy[d + 1]][j + dx[d + 1]] = input[i + dy[d]][j + dx[d]];
        }
      }
    }
    input = [...visit];
  }
}

input.forEach((e) => console.log(e.join(" ")));
process.exit();
