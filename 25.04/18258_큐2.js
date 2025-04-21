// 2등 코드
let fs = require("fs");
let input = fs
  .readFileSync("./input.txt") // .readFileSync(0)
  .toString()
  .trim();

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

const N = +readToken();
let que = new Queue();
let result = [];

for (let i = 0; i < N; i++) {
  const command = readToken();

  if (command === "push") {
    const num = readToken();
    que.append(num);
  } else if (command === "pop") {
    result.push(que.popleft());
  } else if (command === "size") {
    result.push(que.length);
  } else if (command === "empty") {
    result.push(que.length ? 0 : 1);
  } else if (command === "front") {
    result.push(que.first);
  } else if (command === "back") {
    result.push(que.last);
  }
}

console.log(result.join("\n"));

process.exit();

/*

const fs = require('fs');

const input = fs.readFileSync(0).toString().trim();
const len = input.length;
let pos = 0;

function readToken() {
	const start = pos;
	while (
		pos < len &&
		input[pos] !== '\n' &&
		input[pos] !== '\r' &&
		input[pos] !== ' '
	) {
        pos++;
    }
		
	const token = input.slice(start, pos);
	pos++;

	return token;
}

const N = parseInt(readToken(), 10);

const queue = new Array(N);
let head = 0;
let tail = 0;

const output = [];
for (let i = 0; i < N; i++) {
	const cmd = readToken();
	if (cmd === 'push') {
		const num = readToken();
		queue[tail++] = num;
	} else if (cmd === 'pop') {
		if (head < tail) {
			output.push(queue[head++]);
		} else {
			output.push('-1');
		}
	} else if (cmd === 'size') {
		output.push((tail - head));
	} else if (cmd === 'empty') {
		output.push(head >= tail ? '1' : '0');
	} else if (cmd === 'front') {
		if (head < tail) {
			output.push(queue[head]);
		} else {
			output.push('-1');
		}
	} else if (cmd === 'back') {
		if (head < tail) {
			output.push(queue[tail - 1]);
		} else {
			output.push('-1');
		}
	}
}

console.log(output.join('\n'));

*/
