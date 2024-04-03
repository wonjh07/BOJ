const main = () => {
  class Queue {
    constructor() {
      this.queue = [];
      this.front = 0;
      this.rear = 0;
    }

    append(v) {
      this.queue[this.rear++] = v;
    }

    popleft() {
      const v = this.queue[this.front];
      this.queue[this.front++] = null;
      return v;
    }

    size() {
      return this.rear - this.front;
    }
  }

  let fs = require("fs");
  let input = fs.readFileSync("input.txt").toString().trim().split("\n");
  //let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
  const [s, t] = input[0].split(" ").map(Number);
  if (s === t) return 0;
  const vst = {};
  vst[s] = "";
  const sign = ["*", "+", "/", "-"];

  const q = new Queue();
  q.append([s, ""]);
  while (q.size()) {
    const [n, hst] = q.popleft();
    const graph = [n ** 2, n * 2, 1, 0];
    for (let i = 0; i < 4; i++) {
      if (i === 3 && n === 0) break;
      const temp = [hst, sign[i]].join("");
      if (
        graph[i] <= t &&
        (vst[graph[i]] === undefined ||
          vst[graph[i]].length > temp.length ||
          (vst[graph[i]].length === temp.length && vst[graph[i]] > temp))
      ) {
        vst[graph[i]] = temp;
        if (graph[i] !== t) {
          q.append([graph[i], temp]);
        }
      }
    }
  }
  if (vst[t] === undefined) return -1;
  return vst[t];
};

console.log(main());
