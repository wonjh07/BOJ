/*
let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().trim().split("\n");
// let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const main = () => {
  return;
};

main();
*/
const main = () => {
  const input = require("fs")
    .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
    .split("\n");
  const print = (e) => console.log(JSON.stringify(e, null, 2));

  process.exit();
};

main();

// 직접 포인터를 움직여가면서 입력 받기
const len = input.length;
let pos = 0;
function readToken() {
  while (
    pos < len &&
    (input[pos] === " " || input[pos] === "\n" || input[pos] === "\r")
  )
    pos++;
  const start = pos;
  while (
    pos < len &&
    input[pos] !== " " &&
    input[pos] !== "\n" &&
    input[pos] !== "\r"
  )
    pos++;
  return input.slice(start, pos);
}

// 빠르고 간결한 토큰 리더 (정규표현식 사용으로 느림)
function readToken() {
  while (pos < len && /\s/.test(input[pos])) pos++;
  const start = pos;
  while (pos < len && !/\s/.test(input[pos])) pos++;
  return input.slice(start, pos);
}

// Deque
// 최신 자바스크립트는 객체 해시구조로 되어있어서
// 그냥 []를 써도 괜찮다고함
// 5만 케이스 이상 넘어가면 성능차이가 확실하게 남

class Node {
  constructor(v) {
    this.v = v;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.start = null;
    this.end = null;
    this.size = 0;
  }

  get length() {
    return this.size;
  }

  get first() {
    return this.start ? this.start.v : -1;
  }

  get last() {
    return this.end ? this.end.v : -1;
  }

  append(v) {
    const node = new Node(v);
    if (!this.size) this.start = node;
    else this.end.next = node;
    this.end = node;
    this.size++;
  }

  popleft() {
    if (!this.size) return -1;
    const value = this.start.v;
    this.start = this.start.next;
    this.size--;
    if (!this.start) this.end = null;
    return value;
  }
}

// PriorityQue splice (big o 비효율)
class PriorityQueue {
  constructor() {
    this.queue = [];
    this.size = 0;
  }

  append(item, priority) {
    let added = false;
    const element = { item, priority };
    for (let i = 0; i < this.size; i++) {
      if (element.priority < this.queue[i].priority) {
        this.queue.splice(i, 0, element);
        added = true;
        break;
      }
    }
    if (!added) {
      this.queue.push(element);
    }
    this.size++;
  }

  popleft() {
    if (!this.size) return null;
    this.size--;
    return this.queue.shift().item;
  }

  peek() {
    if (!this.size) return null;
    return this.queue[0].item;
  }

  isEmpty() {
    return this.size === 0;
  }
}

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
