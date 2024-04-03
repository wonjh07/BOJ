// bfs 712ms
const main = () => {
  class Node {
    constructor(y, x) {
      this.y = y;
      this.x = x;
    }
  }

  class Queue {
    constructor() {
      this.front = null;
      this.rear = null;
      this.size = 0;
    }

    length() {
      return this.size;
    }

    append(y, x) {
      let node = new Node(y, x);
      if (this.size === 0) {
        this.front = node;
      } else {
        this.rear.next = node;
      }
      this.rear = node;
      this.size++;
    }

    popleft() {
      let value = this.front;
      if (this.size === 0) {
        this.front = null;
        this.rear = null;
      } else {
        this.front = this.front.next;
      }
      this.size--;
      return value;
    }
  }
  const fs = require("fs");
  let input = fs.readFileSync("input.txt").toString().trim().split("\n");
  //let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
  const [N, M] = input[0].split(" ").map(Number);
  const arr = new Array(N)
    .fill()
    .map((e, i) => input[i + 1].split("").map(Number));
  const ans = new Array(N).fill().map(() => new Array(M).fill(0));
  const cnt = {};
  const dy = [-1, 0, 1, 0];
  const dx = [0, 1, 0, -1];
  let cur_i = -1;

  const bfs = (y, x, cur_i) => {
    const q = new Queue();
    let temp = 1;
    q.append(y, x);
    while (q.length()) {
      const v = q.popleft();
      for (let d = 0; d < 4; d++) {
        const [a, b] = [v.y + dy[d], v.x + dx[d]];
        if (!(0 <= a && a < N && 0 <= b && b < M)) continue;
        if (arr[a][b] === 0) {
          temp += 1;
          arr[a][b] = cur_i;
          q.append(a, b);
        }
      }
    }
    cnt[cur_i] = temp;
  };

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (arr[i][j] === 1) {
        const vst = new Set();
        ans[i][j] += 1;
        for (let d = 0; d < 4; d++) {
          const [a, b] = [i + dy[d], j + dx[d]];
          if (!(0 <= a && a < N && 0 <= b && b < M)) continue;
          const num = arr[a][b];
          if (num < 0) vst.add(num);
          else if (num === 0) {
            arr[a][b] = cur_i;
            bfs(a, b, cur_i);
            vst.add(cur_i);
            cur_i -= 1;
          }
        }
        for (v of vst) {
          ans[i][j] += cnt[v];
        }
        ans[i][j] %= 10;
      }
    }
  }

  for (a of ans) {
    console.log(a.join(""));
  }
  return;
};

main();

/*
// dfs 3448ms
const main = () => {
    const fs = require("fs");
    let input = fs.readFileSync("input.txt").toString().trim().split("\n");
    //let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    const [N, M] = input[0].split(" ").map(Number);
    const arr = new Array(N)
      .fill()
      .map((e, i) => input[i + 1].split("").map(Number));
    const vst = new Array(N)
      .fill()
      .map((e, i) => input[i + 1].split("").map(Number));
    const dy = [0, 1, 0, -1];
    const dx = [1, 0, -1, 0];
    const dfs = (y, x, stack) => {
      let cnt = 0;
      for (let d = 0; d < 4; d++) {
        const [a, b] = [y + dy[d], x + dx[d]];
        if (!(0 <= a && a < N && 0 <= b && b < M)) continue;
        if (arr[a][b] === 0) {
          arr[a][b] = -1;
          cnt += 1 + dfs(a, b, stack);
        } else if (arr[a][b] === 1) {
          stack.add([a, b].join(","));
        }
      }
      return cnt;
    };
  
    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (arr[i][j] === 0) {
          const stack = new Set();
          arr[i][j] = -1;
          const cnt = dfs(i, j, stack) + 1;
          for (s of stack) {
            const [a, b] = s.split(",");
            vst[a][b] += cnt;
            vst[a][b] %= 10;
          }
        }
      }
    }
    for (v of vst) {
      console.log(v.join(""));
    }
    return;
  };
  
  main();
  */


/*
//1등코드
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map((e) => parseInt(e));
const group_size = {};
const map = [];

for(let i = 0; i < N; i++) {
  map.push(Array.from(input[i + 1]).map((e) => parseInt(e)));
}

let number = 2;

const dr = [-1, 1, 0, 0];
const dc = [0, 0, -1, 1];

for(let i = 0; i < N; i++) {
  for(let j = 0; j < M; j++) {
    if (map[i][j] !== 0) continue;
    const size = grouping(i, j, number);
    group_size[number++] = size;
  }
}

const answer = Array.from(new Array(N), () => new Array(M).fill(0));

for(let i = 0; i < N; i++) {
  for(let j = 0; j < M; j++) {
    if (map[i][j] !== 1) continue;
    answer[i][j] = 1;
    const adjNumbers = [];
    for(let k = 0; k < 4; k++) {
      const nr = i + dr[k];
      const nc = j + dc[k];
      if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;

      const adjNumber = map[nr][nc];
      if (adjNumber === 1 || adjNumbers.includes(adjNumber)) continue;
      answer[i][j] += group_size[adjNumber];
      adjNumbers.push(adjNumber);
    }
    answer[i][j] %= 10;
  }
}

console.log(answer.map((e) => e.join('')).join('\n'));

function grouping (r, c, number) {
  map[r][c] = number;

  let cnt = 1;

  for(let k = 0; k < 4; k++) {
    const nr = r + dr[k];
    const nc = c + dc[k];
    if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
    if (map[nr][nc] !== 0) continue; // 이미 방문 or 방문할 수 없는 벽
    cnt += grouping(nr, nc, number);
  }
  return cnt;
}
*/
