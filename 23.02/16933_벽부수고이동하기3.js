const main = () => {
  class Node {
    constructor(y, x, wall, time, cnt) {
      this.y = y;
      this.x = x;
      this.wall = wall;
      this.time = time;
      this.cnt = cnt;
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

    append(y, x, wall, time, cnt) {
      let node = new Node(y, x, wall, time, cnt);
      if (this.size === 0) {
        this.front = node;
      } else {
        this.rear.next = node;
      }
      this.rear = node;
      this.size++;
    }

    popleft() {
      let value = this.front;
      if (this.size === 0) {
        this.front = null;
        this.rear = null;
      } else {
        this.front = this.front.next;
      }
      this.size--;
      return value;
    }
  }

  const fs = require("fs");
  let input = fs.readFileSync("input.txt").toString().trim().split("\n");
  //let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
  const [N, M, K] = input[0].split(" ").map(Number);
  if (N === 1 && M === 1) return 1;
  const arr = new Array(N)
    .fill()
    .map((e, i) => input[i + 1].split("").map(Number));
  const vst = new Array(N).fill().map(() => new Array(M).fill(Infinity));
  const dy = [0, 1, 0, -1];
  const dx = [1, 0, -1, 0];
  vst[0][0] = 0;
  const [a, b] = [N - 1, M - 1];
  const q = new Queue();
  q.append(0, 0, 0, true, 2);
  while (q.length()) {
    const op = q.popleft();
    const [y, x, wall, time, cnt] = [op.y, op.x, op.wall, op.time, op.cnt];
    let rest = false;
    for (let i = 0; i < 4; i++) {
      const [ny, nx] = [y + dy[i], x + dx[i]];
      if (ny === a && nx === b) return cnt;
      if (!(0 <= ny && ny < N && 0 <= nx && nx < M)) continue;
      const temp = wall + arr[ny][nx];
      if (temp <= K && vst[ny][nx] > temp) {
        if (time === false && arr[ny][nx] === 1) {
          rest = true;
          continue;
        }
        vst[ny][nx] = temp;
        q.append(ny, nx, temp, !time, cnt + 1);
      }
    }
    if (rest) q.append(y, x, wall, !time, cnt + 1);
  }
  return -1;
};

console.log(main());
