// 1등 코드
let fs = require("fs");
let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = +input[0];
const vst = [];
const d = +input[input.length - 1];

// heapq min
class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(val) {
    this.heap.push(val);
    this._bubbleUp();
  }

  popLeft() {
    if (this.heap.length === 1) return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this._bubbleDown();
    return min;
  }

  _bubbleUp() {
    let index = this.heap.length - 1;
    const current = this.heap[index];

    while (index > 0) {
      let parentIdx = Math.floor((index - 1) / 2);
      if (this.heap[parentIdx] <= current) break;

      [this.heap[parentIdx], this.heap[index]] = [
        this.heap[index],
        this.heap[parentIdx],
      ];
      index = parentIdx;
    }
  }

  _bubbleDown() {
    let index = 0;
    const length = this.heap.length;

    while (true) {
      let left = 2 * index + 1;
      let right = 2 * index + 2;
      let smallest = index;

      if (left < length && this.heap[left] < this.heap[smallest])
        smallest = left;
      if (right < length && this.heap[right] < this.heap[smallest])
        smallest = right;

      if (smallest === index) break;

      [this.heap[index], this.heap[smallest]] = [
        this.heap[smallest],
        this.heap[index],
      ];
      index = smallest;
    }
  }

  get size() {
    return this.heap.length;
  }

  get peek() {
    return this.heap[0];
  }
}

for (let i = 1; i <= N; i++) {
  let [st, ed] = input[i].split(" ").map(Number);
  if (st > ed) {
    const temp = st;
    st = ed;
    ed = temp;
  }
  if (ed - st > d) continue;
  vst.push([st, ed]);
}

vst.sort((a, b) => a[1] - b[1] || a[0] - b[0]);

let ans = 0;
let q = new MinHeap();

for (let i = 0; i < vst.length; i++) {
  let [st, ed] = vst[i];
  q.push(st);

  while (q.size) {
    if (q.peek >= ed - d) break;
    q.popLeft();
  }

  ans = Math.max(ans, q.size);
}

console.log(ans);
