let fs = require("fs");
let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const N = +input[0];

const mod = 1000000007n;
const foods = input[1]
  .trim()
  .split(" ")
  .map(BigInt)
  .sort((a, b) => (a < b ? -1 : 1));

let pow2 = new Array(N).fill(1n);
for (let i = 1; i < N; i++) {
  pow2[i] = (pow2[i - 1] * 2n) % mod;
}

let ans = 0n;
for (let i = 0; i < N; i++) {
  ans = (ans + ((foods[i] * (pow2[i] - pow2[N - i - 1] + mod)) % mod)) % mod;
}

console.log(ans.toString());

/*
1등 코드
var input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
var N = +(input[0]);
var scrobil = input[1].split(' ').map(x => +x).sort((a,b) => a-b);
var total = 0n;
var p = 1000000007n;
var v = 1n;
var list = [1n];
for (var i = 1; i < 300000; i++) {
    v *= 2n;
    v %= p;
    list.push(v);
}
for (var i = 0; i < N-1; i++) {
    var d = scrobil[i+1]-scrobil[i];
    if (d === 0) continue;
    var cnt = ((list[i+1]-1n+p)%p*(list[N-(i+1)]-1n+p)%p)%p;
    total += cnt*BigInt(d);
    total %= p;
}
console.log(String(total));

*/
