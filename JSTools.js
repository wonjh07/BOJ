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

  popleft() {
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
