const main = () => {
  let fs = require("fs");
  let input = fs.readFileSync("input.txt").toString().trim().split("\n");
  // let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

  class Queue {
    constructor() {
      this.queue = [];
      this.front = 0;
      this.rear = 0;
    }
    append(value) {
      this.queue[this.rear++] = value;
    }
    popleft() {
      const value = this.queue[this.front];
      delete this.queue[this.front];
      this.front++;
      return value;
    }
    size() {
      return this.rear - this.front;
    }
  }

  const INF = Infinity;
  const N = +input[0];
  const [r1, c1, r2, c2] = input[1].split(" ").map((e) => +e);
  const dy = [-2, -2, 0, 0, 2, 2];
  const dx = [-1, 1, -2, 2, -1, 1];

  const bfs = () => {
    const vst = new Array(N).fill().map(() => new Array(N).fill(INF));
    const q = new Queue();
    q.append([r1, c1, 1]);

    while (q.size()) {
      const [r, c, n] = q.popleft();
      for (let i = 0; i < 6; i++) {
        let [a, b] = [r + dy[i], c + dx[i]];
        if (0 <= a && a < N && 0 <= b && b < N) {
          if (vst[a][b] > n) {
            vst[a][b] = n;
            q.append([a, b, n + 1]);
            if (a == r2 && b == c2) {
              return n;
            }
          }
        }
      }
    }

    return -1;
  };

  console.log(bfs());
};

main();
/*
  1등 코드
  const fs = require('fs')
  const filePath = process.platform === 'linux' ? '/dev/stdin' : __dirname + '/input.txt'
  const fileEnter = process.platform === 'linux' ? '\n' : '\r\n'
  const input = fs.readFileSync(filePath).toString().split(fileEnter)
  
  const N = +input[0]
  const graph = []
  const [a, b, c, d] = input[1].split(' ').map(Number)
  for(let i =0 ;i<N;i++){
      graph.push(new Array(N).fill(0))
  }
  
  dx = [-2, -2, 0, 0, 2, 2]
  dy = [-1, 1, -2, 2, -1, 1]
  
  const BFS = (x, y) => {
      let queue = [[Number(x), Number(y)]]
      graph[x][y] = 1
  
      while(queue.length){
          let [x, y] = queue.shift()
          for(let i = 0; i< 6; i++){
              nx = x + dx[i]
              ny = y + dy[i]
  
              if(nx < 0 || ny < 0 || nx >= N || ny >= N || graph[nx][ny] !== 0){
                  continue
              }
              if(graph[nx][ny] === 0){
                  graph[nx][ny] += graph[x][y] + 1
                  queue.push([nx, ny])
              }
          }
      }
      
  }
  
  BFS(a, b)
  console.log(graph[c][d] -1)
  
  */
