let input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split(" ");

const S = +input[0];
const nums = input[1].split("");
const W = S + 2;
const H = 2 * S + 3;
const HalfH = parseInt(H / 2);
const container = new Array(H).fill("");
const printNums = (num) => {
  const arr = new Array(H).fill().map((_) => new Array(W).fill(" "));

  const makeHorizon = (order) => {
    i = {
      1: 0,
      2: HalfH,
      3: H - 1,
    };
    for (let j = 1; j < W - 1; j++) {
      arr[i[order]][j] = "-";
    }
  };

  const makeVertical = (order) => {
    j = {
      1: 0,
      2: 0,
      3: W - 1,
      4: W - 1,
    };

    start = {
      1: 1,
      2: HalfH + 1,
      3: 1,
      4: HalfH + 1,
    };
    for (let i = start[order]; i < start[order] + HalfH - 1; i++) {
      arr[i][j[order]] = "|";
    }
  };

  if (![1, 4].includes(num)) makeHorizon(1);
  if (![1, 7, 0].includes(num)) makeHorizon(2);
  if (![1, 4, 7].includes(num)) makeHorizon(3);
  if (![1, 2, 3, 7].includes(num)) makeVertical(1);
  if ([2, 6, 8, 0].includes(num)) makeVertical(2);
  if (![5, 6].includes(num)) makeVertical(3);
  if (num !== 2) makeVertical(4);

  for (let ii = 0; ii < H; ii++) {
    for (let jj of arr[ii]) {
      container[ii] += jj;
    }
    container[ii] += " ";
  }
};

nums.forEach((num) => {
  printNums(+num);
});

container.map((e) => console.log(e));
