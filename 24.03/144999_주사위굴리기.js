let [[N, M, y, x, R], ...input] = require("fs")
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

const orders = input.pop();
let dice = [0, 0, 0, 0, 0, 0];
const dy = [0, 0, 0, -1, 1];
const dx = [0, 1, -1, 0, 0];

for (let order of orders) {
  const [ty, tx] = [y + dy[order], x + dx[order]];
  if (ty < 0 || N <= ty || tx < 0 || M <= tx) continue;
  [y, x] = [ty, tx];

  const [up, forward, right, backward, left, down] = dice;
  if (order === 1) dice = [left, forward, up, backward, down, right];
  else if (order === 2) dice = [right, forward, down, backward, up, left];
  else if (order === 3) dice = [backward, up, right, down, left, forward];
  else if (order === 4) dice = [forward, down, right, up, left, backward];

  if (input[y][x] === 0) {
    input[y][x] = dice[5];
  } else {
    dice[5] = input[y][x];
    input[y][x] = 0;
  }

  console.log(dice[0]);
}
process.exit();
