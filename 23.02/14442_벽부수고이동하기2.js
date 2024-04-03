const main = () => {
  class Queue {
    constructor() {
      this.queue = [];
      this.front = 0;
      this.rear = 0;
    }

    append(v) {
      this.queue[this.rear++] = v;
    }

    popleft() {
      const v = this.queue[this.front];
      this.queue[this.front++] = null;
      return v;
    }

    size() {
      return this.rear - this.front;
    }
  }

  const fs = require("fs");
  let input = fs.readFileSync("input.txt").toString().trim().split("\n");
  //let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
  const [N, M, K] = input[0].split(" ").map(Number);
  if (N === 1 && M === 1) return 1;
  const arr = new Array(N)
    .fill()
    .map((e, i) => input[i + 1].split("").map(Number));
  const vst = new Array(N).fill().map(() => new Array(M).fill(Infinity));
  const cnt = new Array(N).fill().map(() => new Array(M).fill(0));
  const dy = [0, 1, 0, -1];
  const dx = [1, 0, -1, 0];
  vst[0][0] = 0;
  cnt[0][0] = 1;
  const [a, b] = [N - 1, M - 1];
  const q = new Queue();
  q.append([0, 0, 0]);
  while (q.size()) {
    const [y, x, wall] = q.popleft();
    for (let i = 0; i < 4; i++) {
      const [ny, nx] = [y + dy[i], x + dx[i]];
      if (ny === a && nx === b) return cnt[y][x] + 1;
      if (!(0 <= ny && ny < N && 0 <= nx && nx < M)) continue;
      const temp = wall + arr[ny][nx];
      if (temp <= K && vst[ny][nx] > temp) {
        vst[ny][nx] = temp;
        cnt[ny][nx] = cnt[y][x] + 1;
        q.append([ny, nx, temp]);
      }
    }
  }
  return -1;
};

console.log(main());

/*
1등코드
class Node{
    constructor(x,y,z,c) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.c = c;
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
    
    push(x,y,z,c) {
        let node = new Node(x,y,z,c);
        if(this.size === 0) {
            this.front = node;
        } else {
            this.rear.next = node;
        }
        this.rear = node;
        this.size++
    } 
    
    pop_left() {
        let value = this.front;
        if(this.size === 0) {
            this.front = null;
            this.rear = null;
        } else {
            this.front = this.front.next;
        }
        this.size--;
        return value;
    }
}

const fs = require('fs');
let inputData = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let[N,M,K] = inputData[0].trim().split(' ').map(Number);
let map = Array.from(Array(N), () => Array(M));
let visited_min = Array.from(Array(N), () => Array(M).fill(K+1));

for(let i=1; i<inputData.length; i++) {
    let input = inputData[i].trim().split('').map(Number);
    for(let j=0; j<input.length; j++) {
        map[i-1][j] = input[j];
    }
}

console.log(BFS());
function BFS() {
    let que = new Queue();
    que.push(0, 0, 0, 1); //x,y,벽 부신 개수, count
    let wx = [0, 0, -1, 1];
    let wy = [-1, 1, 0, 0];
    while(que.length()) {
        let v = que.pop_left();
        if((v.x===M-1) && (v.y===N-1)) {
            return v.c;
        }
        for(let i=0; i<4; i++) {
            let nx = v.x + wx[i];
            let ny = v.y + wy[i];
            if((nx>=0 && nx<=M-1) && (ny>=0 && ny<=N-1)) {
                if(map[ny][nx] === 0) {
                    if(visited_min[ny][nx] > v.z) {
                        visited_min[ny][nx] = v.z;
                        que.push(nx,ny,v.z,v.c+1);
                    }
                } else {
                    //벽을 만났을때
                    if(visited_min[ny][nx] > v.z+1) {
                        visited_min[ny][nx] = v.z+1;
                        que.push(nx,ny,v.z+1,v.c+1);
                    }
                }
            }
        }
    }
    return -1;
}
*/
