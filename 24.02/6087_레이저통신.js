let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");
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
  const INF = Infinity;
  let [W, H] = input[0].split(" ").map(Number);
  const arr = new Array(H).fill().map((_, i) => input[i + 1].split(""));
  const vst = new Array(H)
    .fill()
    .map(() => new Array(W).fill().map(() => [INF, INF, INF, INF]));
  const dx = [1, 0, -1, 0]; // 동, 남, 서, 북 => 0, 1, 2, 3
  const dy = [0, -1, 0, 1];
  let answer = INF;

  const findC = () => {
    for (let i = 0; i < H; i++) {
      for (let j = 0; j < W; j++) {
        if (arr[i][j] === "C") {
          arr[i][j] = "S";
          return [i, j];
        }
      }
    }
  };
  const [sy, sx] = findC();

  const q = new Queue();
  for (let d = 0; d < 4; d++) {
    const [ty, tx] = [sy + dy[d], sx + dx[d]];
    if (0 <= ty && ty < H && 0 <= tx && tx < W && arr[ty][tx] !== "*") {
      vst[ty][tx][d] = 0;
      q.append([ty, tx, d, 0]);
    }
  }

  while (q.length()) {
    const [y, x, dc, cnt] = q.popLeft();
    if (answer <= cnt) continue;
    for (let d = 0; d < 4; d++) {
      if (Math.abs(d - dc) === 2) continue;
      const now = dc !== d ? cnt + 1 : cnt;
      const [ty, tx] = [y + dy[d], x + dx[d]];

      if (0 > ty || ty >= H || 0 > tx || tx >= W || arr[ty][tx] === "*")
        continue;

      if (arr[ty][tx] === "C") {
        if (answer > now) answer = now;
        continue;
      }

      if (arr[ty][tx] === "." && vst[ty][tx][d] > now) {
        vst[ty][tx][d] = now;
        q.append([ty, tx, d, now]);
      }
    }
  }
  console.log(answer);
  return;
};

main();
