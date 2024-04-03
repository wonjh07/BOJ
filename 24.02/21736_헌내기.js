let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n");
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

class Node {
  constructor(e) {
    this.e = e;
  }
}

class Queue {
  constructor() {
    this.front = null;
    this.rear = null;
    this.size = 0;
  }

  length() {
    return this.size;
  }

  append(e) {
    let node = new Node(e);
    if (this.size === 0) this.front = node;
    else this.rear.next = node;
    this.rear = node;
    this.size++;
  }

  popLeft() {
    if (this.size === 0) return;
    let value = this.front.e;
    this.size--;

    if (this.size === 0) {
      this.front = null;
      this.rear = null;
    } else this.front = this.front.next;
    return value;
  }
}

const main = () => {
  const [N, M] = input[0].split(" ").map(Number);
  const arr = new Array(N).fill().map((_, i) => input[i + 1].split(""));
  const findStart = () => {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (arr[i][j] == "I") return [i, j];
      }
    }
  };
  const dx = [1, 0, -1, 0];
  const dy = [0, -1, 0, 1];
  let answer = 0;

  const start = findStart();
  const q = new Queue();
  q.append(start);

  while (q.length()) {
    const [y, x] = q.popLeft();
    for (let d = 0; d < 4; d++) {
      const [ty, tx] = [y + dy[d], x + dx[d]];
      if (0 > ty || ty >= N || 0 > tx || tx >= M || arr[ty][tx] === "X")
        continue;
      if (arr[ty][tx] === "P") answer++;
      arr[ty][tx] = "X";
      q.append([ty, tx]);
    }
  }

  if (answer === 0) console.log("TT");
  else console.log(answer);
  return;
};

main();

/* 
1등 코드

let [NM, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let [N, M] = NM.split(' ').map(x=>+x);
let board = Array.from({length:N}, (_, i) => input[i].split(''));

let cnt = 0;
getAnswer();

function getAnswer() {
    
for (let n = 0; n < N; ++n) {
    for (let m = 0; m < M; ++m) {
        if (board[n][m] === 'I') {
            dps(m, n);
            console.log(cnt>0?cnt : 'TT');
            return;
        }
    }
}

};

function dps(x, y) {
    if (board[y][x] === 'X') return;

    const a = board[y][x];
    board[y][x] = 'X';
    if (a === 'P') {cnt++;}

    if (x-1 >= 0) dps(x-1, y);
    if (y-1 >= 0) dps(x, y-1);
    if (x+1 < M) dps(x+1, y);
    if (y+1 < N) dps(x, y+1);
}

*/