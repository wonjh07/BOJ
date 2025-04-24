let input = require("fs")
  .readFileSync("./input.txt") // .readFileSync(0)
  .toString()
  .trim()
  .split("\n");

function main() {
  let N = +input[0];
  let cost = input.slice(1).map((s) => s.split(" ").map(Number));
  const INF = Infinity;
  const dp = Array.from({ length: N }, () => Array(1 << N).fill(-1));
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (cost[i][j] === 0) cost[i][j] = INF;
    }
  }
  function dfs(vst, i) {
    if (vst === (1 << N) - 1) return cost[i][0] || INF;
    if (dp[i][vst] > -1) return dp[i][vst];

    dp[i][vst] = INF;
    for (let j = 1; j < N; j++) {
      if (vst & (1 << j)) continue;
      const tmp = dfs(vst | (1 << j), j) + cost[i][j];
      dp[i][vst] = Math.min(dp[i][vst], tmp);
    }

    return dp[i][vst];
  }

  console.log(dfs(1, 0));
  process.exit();
}
main();

/*
1등 코드
const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

function solve() {
    const INF = 100_000_000;
    const N = +input[0];
    const W = input.slice(1).map(s => s.split(' ').map(Number));
    const minCost = Array.from({length: N}, () => Array(1 << N).fill(-1));
    for (let i=0 ; i<N ; i++) {
        for (let j=0 ; j<N ; j++) {
            if (W[i][j] === 0) W[i][j] = INF;
        }
    }

    // 현재 here에 있고, visited에 방문한 도시들이 주어질때, 남은 도시들을 방문하는 최소 비용 반환
    function travel(here, visited) {
        if (visited === (1 << N) - 1) {
            return minCost[here][visited] = W[here][0];
        }

        if (minCost[here][visited] !== -1) return minCost[here][visited];

        let min = INF;
        for (let next=1 ; next<N ; next++) {
            if ((visited & (1 << next))) continue;
            min = Math.min(min, travel(next, visited | (1 << next)) + W[here][next]);
        }
        return minCost[here][visited] = min;
    }

    return travel(0, 1);
}

console.log(solve());
*/
