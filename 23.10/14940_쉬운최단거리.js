let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n");
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const main = () => {
  class Node {
    constructor(e) {
      this.e = e;
    }
  }

  class Deque {
    constructor() {
      this.front = null;
      this.back = null;
      this.size = 0;
    }

    length() {
      return this.size;
    }

    append(e) {
      let node = new Node(e);
      if (this.size === 0) this.front = node;
      else this.back.next = node;
      this.back = node;
      this.size++;
    }

    popleft() {
      if (this.size === 0) return;
      const value = this.front;
      this.size--;

      if (this.size === 0) {
        this.front = null;
        this.rear = null;
      } else this.front = this.front.next;

      return value.e;
    }
  }

  const findStart = () => {
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (arr[i][j] === 2) return [i, j];
      }
    }
  };

  const [N, M] = input[0].split(" ").map(Number);
  const arr = new Array(N)
    .fill()
    .map((_, i) => input[i + 1].split(" ").map((e) => (e === "1" ? -1 : +e)));
  const [sy, sx] = findStart();

  const q = new Deque();
  q.append([sy, sx, 1]);
  arr[sy][sx] = 0;

  const dx = [1, 0, -1, 0];
  const dy = [0, 1, 0, -1];

  while (q.length()) {
    const [y, x, now] = q.popleft();

    for (let d = 0; d < 4; d++) {
      const [ty, tx] = [y + dy[d], x + dx[d]];
      if (!(0 <= ty && ty < N && 0 <= tx && tx < M)) continue;

      if (arr[ty][tx] === -1 || arr[ty][tx] > now) {
        arr[ty][tx] = now;
        q.append([ty, tx, now + 1]);
      }
    }
  }

  arr.forEach((e) => console.log(e.join(" ")));

  return;
};

main();


/*
1등 코드 284ms

const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(v => +v);

const matrix = [];

let start;
for (let i = 1; i <= n; i++){
    matrix.push(input[i].split(' ').map((v, j) => {
        v = +v;
        if (v === 2){
            start = [i - 1 , j];
        }
        return v;
    }));
}

const dx = [-1, 0, 1, 0];
const dy = [0, -1, 0, 1];

const bfs = (node) => {
    const queue = [node];
    while (queue.length){
        const [x, y] = queue.shift();
        for (let i = 0; i < 4; i++){
            const nx = x + dx[i];
            const ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (matrix[nx][ny] === 1){
                matrix[nx][ny] = matrix[x][y] + 1;
                queue.push([nx, ny]);
            }
        }
    }
}

const markUnreachable = () => {
    for (let i = 0; i < matrix.length; i++){
        matrix[i] = matrix[i].map(v => v === 1 ? -1 : v);
    }
    return matrix;
}

// 시작점 주변 조작
const restoreStart = (start) => {
    const [x, y] = start;
    for (let i = 0; i < 4; i++){
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
        if (matrix[nx][ny] !== 0){
            matrix[nx][ny] = 1;
        }
    }
}


matrix[start[0]][start[1]] = 0;
bfs(start);
markUnreachable();
restoreStart(start);

console.log(matrix.map(v => v.join(' ')).join('\n'));

*/