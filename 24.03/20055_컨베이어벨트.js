const input = require("fs")
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

const belts = input[1];
const [N, K] = input[0];
const len = 2 * N;
const vst = new Array(len).fill(0);
const robots = new Array(len).fill(0);
let [start, end] = [0, N - 1];
let retiredBelt = 0;
let stage = 0;

const moveBelt = () => {
  start -= 1;
  end -= 1;
  if (start < 0) start += len;
  if (end < 0) end += len;
  robots[end] = 0;
};

const moveRobot = () => {
  const inspectBelt = (idx) => {
    if (belts[idx] === 0 && !vst[idx]) {
      retiredBelt += 1;
      vst[idx] = 1;
    }
  };
  let now = end - 1;
  let next = end;

  while (1) {
    if (now < 0) now += len;
    if (now === start) break;

    if (robots[now] && belts[next] && !robots[next]) {
      robots[next] = 1;
      robots[now] = 0;
      belts[next] -= 1;
      inspectBelt(next);
    }

    [now, next] = [now - 1, now];
  }

  robots[end] = 0;

  if (belts[start] > 0) {
    belts[start] -= 1;
    robots[start] = 1;
    inspectBelt(start);
  }
};

while (retiredBelt < K) {
  moveBelt();
  moveRobot();
  stage += 1;
}

console.log(stage);
process.exit();
