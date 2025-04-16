// 1등코드 달성
let input = require("fs")
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M] = input.shift().split(" ");
input = input.map((e) => e.split(" "));

const q = [];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    input[i][j] = +input[i][j];
    if (input[i][j]) q.push([i, j]);
  }
}

const dy = [0, 1, 1, 1, 0, -1, -1, -1];
const dx = [1, 1, 0, -1, -1, -1, 0, 1];

while (q.length) {
  const [y, x] = q.shift();
  const now = input[y][x];
  for (let d = 0; d < 8; d++) {
    const ty = y + dy[d];
    const tx = x + dx[d];
    if (ty < 0 || N <= ty || tx < 0 || M <= tx || input[ty][tx]) continue;
    input[ty][tx] = now + 1;
    q.push([ty, tx]);
  }
}

let ans = 0;
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (input[i][j] > ans) ans = input[i][j];
  }
}

console.log(ans - 1);
process.exit();

/* 1등코드
 
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
  
const [n, m] = input.shift().split(' ');

input = input.map((row) => row.split(' '));

const sharks = [];
const dx = [-1, -1, -1, 0, 0, 1, 1, 1];
const dy = [-1, 0, 1, -1, 1, -1, 0, 1];
// 상어 좌표 찾기
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    input[i][j] = Number(input[i][j]);
    if (input[i][j] === 1) {
      sharks.push([i, j]);
    }
  }
}

// bfs 돌면서 input값 바꾸기
while (sharks.length > 0) {
  const tmp = [];
  while (sharks.length > 0) {
    const [x, y] = sharks.shift();
    const num = input[x][y];
    for (let i = 0; i < 8; i++) {
      const nextX = x + dx[i];
      const nextY = y + dy[i];
      // 좌표 검증 및 이미 값이 있는지
      if (
        nextX < 0 ||
        nextX >= n ||
        nextY < 0 ||
        nextY >= m ||
        input[nextX][nextY] !== 0
      ) {
        continue;
      }
      input[nextX][nextY] = num + 1;
      tmp.push([nextX, nextY]);
    }
  }
  sharks.push(...tmp);
}

// 배열 최대값 찾아서 -1 출력
let _max = 0;
input.forEach((row) => (_max = Math.max(_max, Math.max(...row))));
console.log(_max - 1);
*/

/* 2등코드
const fs = require('fs');
let [info, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let [N, M] = info.split(' ').map(Number);
let board = input.map((v) => v.split(' ').map(Number));
let dx = [-1, -1, -1, 0, 1, 1, 1, 0];
let dy = [-1, 0, 1, 1, 1, 0, -1, -1];
let queue = [];
for(let i=0; i<N; i++) {
    for(let j=0; j<M; j++) {
        if(board[i][j] === 1) queue.push([i, j]);
    }
}
while(queue.length) {
    let [x, y] = queue.shift();
    for(let i=0; i<8; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        if(nx >= 0 && ny >= 0 && nx < N && ny < M) {
            if(board[nx][ny] === 0) {
                board[nx][ny] = board[x][y] + 1;
                queue.push([nx, ny]);
            }
        }
    }
}
let ans = 0;
for(let i=0; i<N; i++) {
    for(let j=0; j<M; j++) {
        if(board[i][j] > ans) ans = board[i][j];
    }
}
console.log(ans - 1);
*/
