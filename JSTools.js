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

// Deque
// 최신 자바스크립트는 객체 해시구조로 되어있어서
// 그냥 []를 써도 괜찮다고함

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

  length() {
    return this.size;
  }

  append(v) {
    const node = new Node(v);
    if (this.size === 0) this.start = node;
    else this.end.next = node;
    this.end = node;
    this.size++;
  }

  popleft() {
    if (this.size === 0) return false;
    const value = this.start.v;
    this.size--;

    if (this.size === 0) {
      this.start = null;
      this.end = null;
    } else this.start = this.start.next;
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
