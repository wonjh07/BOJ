let input = require("fs")
  .readFileSync("./input.txt") // .readFileSync(0)
  .toString()
  .trim()
  .split("\n");

let N = +input[0];
let board = [];
let dia1 = Array(2 * N).fill(false);
let dia2 = Array(2 * N).fill(false);
let ansW = 0;
let ansB = 0;
for (let i = 1; i <= N; i++) {
  board.push(input[i].split(" ").map(Number));
}

function check(i, j) {
  return !dia1[i + j] && !dia2[i - j + (N - 1)];
}
function addV(i, j) {
  dia1[i + j] = true;
  dia2[i - j + (N - 1)] = true;
}
function removeV(i, j) {
  dia1[i + j] = false;
  dia2[i - j + (N - 1)] = false;
}

function dfsWhite(i, j, now) {
  if (i >= N) {
    ansW = Math.max(ansW, now);
    return;
  }

  const nj = i % 2 ? 0 : 1;
  if (board[i][j] && check(i, j)) {
    addV(i, j);
    j + 2 >= N ? dfsWhite(i + 1, nj, now + 1) : dfsWhite(i, j + 2, now + 1);
    removeV(i, j);
  }

  j + 2 >= N ? dfsWhite(i + 1, nj, now) : dfsWhite(i, j + 2, now);
}

function dfsBlack(i, j, now) {
  if (i >= N) {
    ansB = Math.max(ansB, now);
    return;
  }

  const nj = i % 2 ? 1 : 0;
  if (board[i][j] && check(i, j)) {
    addV(i, j);
    j + 2 >= N ? dfsBlack(i + 1, nj, now + 1) : dfsBlack(i, j + 2, now + 1);
    removeV(i, j);
  }

  j + 2 >= N ? dfsBlack(i + 1, nj, now) : dfsBlack(i, j + 2, now);
}

dfsWhite(0, 0, 0);
dfsBlack(0, 1, 0);

console.log(ansW + ansB);
