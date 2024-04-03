let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const dy = [0, 1, 0, -1];
const dx = [1, 0, -1, 0];
const arr = input.splice(1).map((e) => e.split(" ").map(Number));
const [N, M] = input[0].split(" ").map(Number);
let answer = N * M * 2;

for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    for (let d = 0; d < 4; d++) {
      const [ty, tx] = [i + dy[d], j + dx[d]];
      if (ty < 0 || N <= ty || tx < 0 || M <= tx) continue;
      if (arr[i][j] < arr[ty][tx]) answer += arr[ty][tx] - arr[i][j];
    }
  }
}

for (let j = 0; j < M; j++) {
  answer += arr[0][j];
  answer += arr[N - 1][j];
}

for (let i = 0; i < N; i++) {
  answer += arr[i][0];
  answer += arr[i][M - 1];
}

console.log(answer);
process.exit();

/* 1등코드

const fs = require('fs')
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
const [n, m] = input[0].split(' ').map(Number)
input.shift()

const arr = input.map(res => res.split(' ').map(Number))

let total = n * m * 2

for(let i = 0; i < n; i++) {
    for(let j = 0; j < m;  j++) {
        if(j != 0) total += Math.abs(arr[i][j] - arr[i][j-1])
        if(j == 0) total += arr[i][j]
        if(j == m - 1) total += arr[i][j]
    }
}

for(let i = 0; i < m; i++) {
    for(let j = 0; j < n;  j++) {
        if(j != 0) total += Math.abs(arr[j][i] - arr[j - 1][i])
        if(j == 0) total += arr[j][i]
        if(j == n - 1) total += arr[j][i]
    }
}

console.log(total)

*/