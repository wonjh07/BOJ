// 2등코드
let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [V, E] = input.shift().split(" ").map(Number);
let parrent = new Array(V + 1).fill().map((_, i) => i);

let arr = input
  .map((row) => row.split(" ").map(Number))
  .sort((a, b) => a[2] - b[2]);

let cost = 0;
let cnt = 0;

const get_parrent = (idx) => {
  if (parrent[idx] !== idx) {
    const result = get_parrent(parrent[idx]);
    parrent[idx] = result;
    return result;
  } else return idx;
};

const union = (v1, v2) => {
  const a = get_parrent(v1);
  const b = get_parrent(v2);
  if (a == b) return false;

  if (a > b) parrent[a] = b;
  else parrent[b] = a;

  return true;
};

for (let i = 0; i < E; i++) {
  const [v1, v2, n] = arr[i];

  if (union(v1, v2)) {
    cnt += 1;
    cost += n;
  }

  if (cnt === V - 1) break;
}

console.log(cost);
process.exit();
