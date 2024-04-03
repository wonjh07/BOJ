const main = () => {
  class Queue {
    constructor() {
      this.queue = [];
      this.front = 0;
      this.rear = 0;
    }

    append(value) {
      this.queue[this.rear++] = value;
    }

    popleft() {
      const value = this.queue[this.front];
      delete this.queue[this.front];
      this.front++;
      return value;
    }

    size() {
      return this.rear - this.front;
    }
  }

  let fs = require("fs");
  let input = fs.readFileSync("input.txt").toString().trim().split("\n");
  //let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
  const mem = new Array(1501).fill().map(() => new Array(1501).fill(0));
  const [A, B, C] = input[0]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  const q = new Queue();
  q.append([A, B, C]);

  if ((A + B + C) % 3 !== 0) {
    return 0;
  }

  while (q.size()) {
    const e = q.popleft();
    if (e[0] === e[1] && e[1] === e[2]) {
      return 1;
    }

    for (let i = 0; i < 3; i++) {
      for (let j = i + 1; j < 3; j++) {
        const [a, b, c] = [e[i], e[j], e[3 - i - j]];
        if (a < b) {
          const res = [a + a, b - a, c].sort((a, b) => a - b);
          if (mem[res[0]][res[1]] === 0) {
            q.append(res);
            mem[res[0]][res[1]] = 1;
          }
        }
      }
    }
  }
  return 0;
};

console.log(main());
