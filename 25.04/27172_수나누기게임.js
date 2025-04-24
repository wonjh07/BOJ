let input = require("fs")
  .readFileSync("./input.txt") // .readFileSync(0)
  .toString()
  .trim()
  .split("\n");

function main() {
  let N = +input[0];
  let player = input[1].split(" ").map(Number);
  let maxValue = Math.max(...player);
  let score = new Array(N).fill(0);
  let cnt = new Array(maxValue + 1).fill(-1);
  for (let k = 0; k < N; k++) {
    cnt[player[k]] = k;
  }

  for (let i = 1; i <= maxValue; i++) {
    if (cnt[i] === -1) continue;
    for (let j = i * 2; j <= maxValue; j += i) {
      if (cnt[j] === -1) continue;
      score[cnt[i]]++;
      score[cnt[j]]--;
    }
  }
  console.log(score.join(" "));
  process.exit();
}

main();
