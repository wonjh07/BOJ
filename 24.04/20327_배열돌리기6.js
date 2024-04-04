// 1등 코드 달성
const input = require("fs")
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

const [N, R] = input[0];
const size = 2 ** N;
const orders = input.splice(-R);
let arr = input.splice(-(2 ** N));

const orderOne = (l) => {
  if (l === 0) return;
  const ps = 2 ** l; //patternSize
  for (let i = 0; i < size; i += ps) {
    for (let d = 0; d < ps / 2; d++) {
      const t = ps - d - 1; // target
      [arr[i + d], arr[i + t]] = [arr[i + t], arr[i + d]];
    }
  }
};

const orderTwo = (l) => {
  if (l === 0) return;
  const ps = 2 ** l;
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j += ps) {
      for (let d = 0; d < ps / 2; d++) {
        const t = ps - d - 1;
        [arr[i][j + d], arr[i][j + t]] = [arr[i][j + t], arr[i][j + d]];
      }
    }
  }
};

const orderThree = (l) => {
  if (l === 0) return;
  const ps = 2 ** l;
  const temp = new Array(size).fill().map((_) => new Array(size).fill(0));
  for (let i = 0; i < size; i += ps) {
    for (let j = 0; j < size; j += ps) {
      for (let pi = 0; pi < ps; pi++) {
        for (let pj = 0; pj < ps; pj++) {
          temp[i + pj][j + ps - 1 - pi] = arr[i + pi][j + pj];
        }
      }
    }
  }
  arr = temp;
};

const orderFour = (l) => {
  if (l === 0) return;
  const ps = 2 ** l;
  const temp = new Array(size).fill().map((_) => new Array(size).fill(0));
  for (let i = 0; i < size; i += ps) {
    for (let j = 0; j < size; j += ps) {
      for (let pi = 0; pi < ps; pi++) {
        for (let pj = 0; pj < ps; pj++) {
          temp[i + ps - 1 - pj][j + pi] = arr[i + pi][j + pj];
        }
      }
    }
  }
  arr = temp;
};

const orderFive = (l) => {
  const ps = 2 ** l;
  for (let i = 0; i < size / 2; i += ps) {
    for (let j = 0; j < size; j += ps) {
      for (let pi = 0; pi < ps; pi++) {
        for (let pj = 0; pj < ps; pj++) {
          [arr[size - ps - i + pi][j + pj], arr[i + pi][j + pj]] = [
            arr[i + pi][j + pj],
            arr[size - ps - i + pi][j + pj],
          ];
        }
      }
    }
  }
};

const orderSix = (l) => {
  const ps = 2 ** l;
  for (let i = 0; i < size; i += ps) {
    for (let j = 0; j < size / 2; j += ps) {
      for (let pi = 0; pi < ps; pi++) {
        for (let pj = 0; pj < ps; pj++) {
          [arr[i + pi][size - ps - j + pj], arr[i + pi][j + pj]] = [
            arr[i + pi][j + pj],
            arr[i + pi][size - ps - j + pj],
          ];
        }
      }
    }
  }
};

const orderSeven = (l) => {
  const ps = 2 ** l;
  const temp = new Array(size).fill().map((_) => new Array(size).fill(0));
  for (let i = 0; i < size; i += ps) {
    for (let j = 0; j < size; j += ps) {
      for (let pi = 0; pi < ps; pi++) {
        for (let pj = 0; pj < ps; pj++) {
          const [ti, tj] = [j, size - ps - i];
          temp[ti + pi][tj + pj] = arr[i + pi][j + pj];
        }
      }
    }
  }
  arr = temp;
};
const orderEight = (l) => {
  const ps = 2 ** l;
  const temp = new Array(size).fill().map((_) => new Array(size).fill(0));
  for (let i = 0; i < size; i += ps) {
    for (let j = 0; j < size; j += ps) {
      for (let pi = 0; pi < ps; pi++) {
        for (let pj = 0; pj < ps; pj++) {
          const [ti, tj] = [size - ps - j, i];
          temp[ti + pi][tj + pj] = arr[i + pi][j + pj];
        }
      }
    }
  }
  arr = temp;
};

for (let [K, l] of orders) {
  if (K === 1) orderOne(l);
  if (K === 2) orderTwo(l);
  if (K === 3) orderThree(l);
  if (K === 4) orderFour(l);
  if (K === 5) orderFive(l);
  if (K === 6) orderSix(l);
  if (K === 7) orderSeven(l);
  if (K === 8) orderEight(l);
}

arr.map((e) => console.log(e.join(" ")));
process.exit();
