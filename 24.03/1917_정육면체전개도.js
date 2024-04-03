// 백준 1등코드 달성
const input = require("fs")
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

const dy = [0, 1, 0, -1];
const dx = [1, 0, -1, 0];
const arr = [[], [], []];
for (let t = 2; t >= 0; t--) {
  arr[t] = input.splice(-6);
}

const main = (T) => {
  const diceMap = arr[T];
  let dice = [0, 0, 0, 0, 0, 0];
  let answer = 0;

  const diceRoll = (order) => {
    const [up, forward, right, backward, left, down] = dice;
    if (order === 0) dice = [right, forward, down, backward, up, left];
    else if (order === 1) dice = [backward, up, right, down, left, forward];
    else if (order === 2) dice = [left, forward, up, backward, down, right];
    else if (order === 3) dice = [forward, down, right, up, left, backward];
  };

  const makeDice = (y, x) => {
    if (!dice[0]) answer += 1;
    dice[0] = 1;
    diceMap[y][x] = 0;
    for (let d = 0; d < 4; d++) {
      const [ty, tx] = [y + dy[d], x + dx[d]];
      if (ty < 0 || 6 <= ty || tx < 0 || 6 <= tx) continue;
      if (diceMap[ty][tx]) {
        diceRoll(d);
        makeDice(ty, tx);
        diceRoll((d + 2) % 4);
      }
    }
  };

  for (let i = 0; i < 6; i++) {
    for (let j = 0; j < 6; j++) {
      if (diceMap[i][j]) {
        makeDice(i, j);
        if (answer === 6) console.log("yes");
        else console.log("no");
        return;
      }
    }
  }
};

for (let T = 0; T < 3; T++) {
  main(T);
}

process.exit();
