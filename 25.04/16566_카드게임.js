let input = require("fs")
  .readFileSync("./input.txt") // .readFileSync(0)
  .toString()
  .trim()
  .split("\n");

const [N, M, K] = input[0].split(" ").map(Number);
const csCards = input[1]
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);
const parrent = new Array(M).fill().map((_, i) => i);
const msCards = input[2].split(" ").map(Number);
let ans = [];

function get_parrent(idx) {
  if (parrent[idx] !== idx) {
    const result = get_parrent(parrent[idx]);
    parrent[idx] = result;
    return result;
  } else return idx;
}

const union = (v1, v2) => {
  const a = get_parrent(v1);
  const b = get_parrent(v2);
  if (a == b) return false;

  if (a < b) parrent[a] = b;
  else parrent[b] = a;

  return true;
};

function bs(target) {
  let [left, right] = [0, M - 1];
  while (left < right) {
    let md = Math.floor((left + right) / 2);

    if (csCards[md] <= target) left = md + 1;
    else right = md;
  }
  return left;
}

for (let msCard of msCards) {
  const resI = get_parrent(bs(msCard));
  ans.push(csCards[parrent[resI]]);
  if (resI < M - 1) union(resI, resI + 1);
}

console.log(ans.join("\n"));

/*
400만 수의 카드
1~N 중 m개의 카드
철수는 빨강 민수는 파랑 (정치색이 확고한듯하다)
k번 서로 카드를 한장골라 내서 큰사람이 이김 (비길수 있다는건가?)
철수 본인이 낼 카드를 마음대로 조작 할 수 있다 (마술사)
민수 철수가 낼 카드를 알수있다 (심리학자)
- 그래서 민수는 철수가 낼 카드보다 큰카드가있다면 가장 근소하게 이기는 카드를냄
K번동안 철수가 낼 카드가 입력으로 주어짐 그렇다면 민수가 어떤 카드를 낼지 출력
*/

/* 
1등코드 - 이분탐색, 분리집합 미사용

const [[n, m, k], cards, queries] = (require("fs").readFileSync(0) + "").trim().split("\n").map((v) => v.split(" ").map(Number));
const next = Array(n + 1).fill(0);
const has = Array(n + 1).fill(false);
for (const v of cards) (next[v - 1] = v), (has[v] = true);
for (let i = n - 1; i > 0; i--) if (next[i] === 0) next[i] = next[i + 1];
const ans = [];
for (const v of queries) {
  let i = next[v];
  while (!has[i]) i = next[i];
  has[i] = false;
  ans.push(i);
}
console.log(ans.join("\n"));

*/

/*
최적화 코드

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M, K] = input[0].split(" ").map(Number);
const MS = input[1].split(" ").map(Number);
const CS = input[2].split(" ").map(Number);

MS.sort((a, b) => a - b);
// console.log(MS);

const parent = [];
for (let i = 0; i <= N; i++) parent[i] = i;
// console.log(parent);

const result = [];
for (const card of CS) {
  let left = 0;
  let right = M - 1;
  let best = -1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (MS[mid] > card) {
      best = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  const idx = getParent(parent, best);
  result.push(MS[idx]);
  // 카드 사용 후 다음 인덱스로 병합
  if (idx < M - 1) {
    unionParent(parent, idx, idx + 1);
  }
}
console.log(result.join("\n"));

function getParent(parent, x) {
  if (parent[x] === x) return x;
  return (parent[x] = getParent(parent, parent[x]));
}

function unionParent(parent, x, y) {
  const rootX = getParent(parent, x);
  const rootY = getParent(parent, y);
  if (rootX !== rootY) {
    parent[rootX] = rootY;
  }
}

*/

/*
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const fs = require("fs");
[nmk, minsu, cheolsu] = fs.readFileSync(filePath).toString().trim().split('\n');

const [n, m, k] = nmk.split(' ').map(Number);
const haved = Array(n + 1).fill(false);

let max = 0;

minsu.split(' ').forEach(element => {
    const num = Number(element);

    haved[num] = true;
    if (max < num) max = num;
});

const parents = Array(n + 1);
for (let i = 1; i <= n; i++) parents[i] = i;

const find = (num) => {
    if(parents[num] === num) return num;
    return parents[num] = find(parents[num]);
}

const union = (num1, num2) => {
    const p1 = find(num1);
    const p2 = find(num2);
    if(p1 > p2) return parents[p2] = p1;
    else return parents[p1] = p2;
}

let parent = max;

for (let i = max - 1; i > 0; i--) {
    if (haved[i]) parent = i;
    
    union(parent, i);
}

const result = [];

cheolsu.split(' ').forEach(element => {
    let current = Number(element);
    if (haved[current]) current++;

    const findParent = find(current);
    result.push(findParent);

    union(findParent, findParent + 1);
});

console.log(result.join('\n'));
*/
