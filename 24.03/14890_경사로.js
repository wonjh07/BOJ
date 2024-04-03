let [[N, L], ...input] = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

let answer = 0;

const validationH = (i) => {
  let stack = 1;
  for (let j = 1; j < N; j++) {
    if (input[i][j - 1] === input[i][j]) {
      stack += 1;
      continue;
    } else if (Math.abs(input[i][j - 1] - input[i][j]) > 1) return false;
    // 높은 경사로 놓을때
    else if (input[i][j - 1] < input[i][j]) {
      if (stack < L) return false;
      stack = 1;
    }
    // 낮은 경사로 놓을떄
    else if (input[i][j - 1] > input[i][j]) {
      if (stack < 0) return false;
      stack = -L + 1;
    }
  }
  if (stack < 0) return false;
  return true;
};

const validationV = (i) => {
  let stack = 1;
  for (let j = 1; j < N; j++) {
    if (input[j - 1][i] === input[j][i]) {
      stack += 1;
      continue;
    } else if (Math.abs(input[j - 1][i] - input[j][i]) > 1) return false;
    // 높은 경사로 놓을때
    else if (input[j - 1][i] < input[j][i]) {
      if (stack < L) return false;
      stack = 1;
    }
    // 낮은 경사로 놓을떄
    else if (input[j - 1][i] > input[j][i]) {
      if (stack < 0) return false;
      stack = -L + 1;
    }
  }
  if (stack < 0) return false;
  return true;
};

for (let a = 0; a < N; a++) {
  if (validationH(a)) answer += 1;
  if (validationV(a)) answer += 1;
}

console.log(answer);
process.exit();
