const main = () => {
  const [N, ...input] = require("fs")
    .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
    .toString()
    .trim()
    .split("\n");

  const arr = input.map((e) => e.split(""));
  const dy = [0, 1, 1, 0, -1, -1];
  const dx = [1, 0, -1, -1, 0, 1];
  let ans = 0;

  const dfs = (i, j, now) => {
    arr[i][j] = now;
    for (let d = 0; d < 6; d++) {
      const [y, x] = [i + dy[d], j + dx[d]];
      if (y < 0 || +N <= y || x < 0 || +N <= x) continue;
      if (arr[y][x] === "X") {
        ans = 2;
        dfs(y, x, 1 - now);
      } else if (arr[y][x] === now) {
        process.exit(console.log(3));
      }
    }
    return;
  };

  for (let i = 0; i < +N; i++) {
    for (let j = 0; j < +N; j++) {
      if (arr[i][j] === "X") {
        ans = Math.max(ans, 1);
        dfs(i, j, 0);
      }
    }
  }
  console.log(ans);
  process.exit();
};

main();
