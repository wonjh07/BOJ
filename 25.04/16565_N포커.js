let fs = require("fs");
let input = fs
  .readFileSync("./input.txt") // .readFileSync(0)
  .toString()
  .trim()
  .split("\n");

const N = +input[0];
let mod = 10007;
let fact = new Array(53).fill(1);
for (let i = 1; i <= 52; i++) {
  fact[i] = (fact[i - 1] * i) % mod;
}

function modPow(a) {
  let res = 1;
  let b = mod - 2;
  a %= mod;
  while (b > 0) {
    if (b % 2 === 1) res = (res * a) % mod;
    a = (a * a) % mod;
    b >>= 1;
  }
  return res;
}

function combi(n, r) {
  if (n < r) return 0;
  return (((fact[n] * modPow(fact[r])) % mod) * modPow(fact[n - r])) % mod;
}

let ans = 0;
for (let k = 1; k <= Math.floor(N / 4); k++) {
  let sign = k % 2 === 1 ? 1 : -1;
  let pairs = combi(13, k);
  let others = combi(52 - 4 * k, N - 4 * k);
  ans = (ans + sign * pairs * others + mod) % mod;
}

if (ans < 0) ans += mod;
console.log(ans);

process.exit();
