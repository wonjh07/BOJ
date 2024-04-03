const solve = () => {
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
      this.back = null;
      this.size = 0;
    }

    length() {
      return this.size;
    }

    append(e) {
      let node = new Node(e);
      if (this.size === 0) {
        this.front = node;
      } else {
        this.back.next = node;
      }
      this.back = node;
      this.size++;
    }

    popleft() {
      const temp = this.front;
      this.size--;
      if (this.size === 0) {
        this.front = null;
        this.back = null;
      } else {
        this.front = this.front.next;
      }
      return temp.e;
    }
  }
  const arr = new Array(8).fill().map((_, i) => input[i].split(""));
  const dx = [0, 0, 1, 1, 1, 0, -1, -1, -1];
  const dy = [0, 1, 1, 0, -1, -1, -1, 0, 1];
  const q = new Queue();
  let now = 0;
  const emptyArr = new Array(8).fill(".");
  q.append([7, 0, 0]);

  while (q.length()) {
    const [y, x, t] = q.popleft();
    if (now != t) {
      now += 1;
    }
    if (now === 8) return 1;
    if (arr[y - now][x] === "#") continue;
    for (let i = 0; i < 8; i++) {
      const [a, b] = [y + dy[i], x + dx[i]];
      if (0 <= a && a <= 7 && 0 <= b && b <= 7 && arr[a - now][b] === ".") {
        if (a === 0 && b === 7) return 1;
        if (7 - a + now === 7) return 1;
        q.append([a, b, t + 1]);
      }
    }
  }
  return 0;
};

console.log(solve());

/*
  1등 코드
  
  const solution = (input) => {
    let answer = false;
    const board = input.map((str) => str.split(""));
    const n = 8;
    const [dx, dy] = [
      [0, 0, 1, -1, 1, -1, 1, -1, 0],
      [1, -1, 0, 0, 1, 1, -1, -1, 0],
    ];
    const q = [];
    const check = Array.from({ length: n }, () =>
      Array.from({ length: n }, () => new Array(n + 1).fill(false))
    );
    check[7][0][0] = true;
    q.push([7, 0, 0]);
  
    while (q.length) {
      const [x, y, t] = q.shift();
      if (x === 0 && y === 7) {
        answer = true;
        break;
      }
      for (let k = 0; k < 9; k++) {
        const [nx, ny] = [x + dx[k], y + dy[k]];
        const nt = Math.min(t + 1, 8);
        if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
        if (nx - t >= 0 && board[nx - t][ny] === "#") continue;
        if (nx - t - 1 >= 0 && board[nx - t - 1][ny] === "#") continue;
        if (check[nx][ny][nt] === false) {
          check[nx][ny][nt] = true;
          q.push([nx, ny, nt]);
        }
      }
    }
  
    if (answer) return 1;
    else return 0;
  };
  
  const fs = require("fs");
  const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
  let input = fs.readFileSync(filePath).toString().trim().split("\n");
  console.log(solution(input));
  */
