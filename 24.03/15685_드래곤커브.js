const input = require("fs")
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(" ").map(Number));

const N = +input[0];
const orders = input.splice(1);
const arr = new Array(101).fill().map((_) => new Array(101).fill(0));
let answer = 0;
const dy = [0, -1, 0, 1];
const dx = [1, 0, -1, 0];

const makeCurve = (y, x, ds, g) => {
  let [ty, tx] = [y, x];
  const temp = [...ds].map((e) => (e + 1) % 4).reverse();
  for (let d of temp) {
    [ty, tx] = [ty + dy[d], tx + dx[d]];
    arr[ty][tx] = 1;
    ds.push(d);
  }
  if (g !== 0) makeCurve(ty, tx, ds, g - 1);
};

for (let order of orders) {
  const [x, y, d, g] = order;
  arr[y][x] = 1;
  const [ty, tx] = [y + dy[d], x + dx[d]];
  arr[ty][tx] = 1;
  if (g !== 0) makeCurve(ty, tx, [d], g - 1);
}

for (let i = 0; i < 100; i++) {
  for (let j = 0; j < 100; j++) {
    if (!arr[i][j]) continue;
    if (arr[i][j] && arr[i + 1][j] && arr[i][j + 1] & arr[i + 1][j + 1]) {
      answer += 1;
    }
  }
}

console.log(answer);
process.exit();

/* 1등코드
function DragonCurve (x, y, d, g) {
  this.initX = x;
  this.initY = y;
  this.direction = d;
  this.generation = g;
  this.points = [[x, y]];
  this.generate(x, y, d, g);
}

DragonCurve.prototype.makeZeroGenerationPoint = function (x, y, d) {

  var point = [x, y];

  switch(d) {
    case 0:
      point[0] += 1;    
      break;
    case 1:
      point[1] -= 1;
      break;
    case 2:
      point[0] -= 1;
      break;
    case 3:
      point[1] += 1;
      break;
    default:
      break;
  }

  return point;
};

DragonCurve.prototype.generate = function (x, y, d, g) {
  for (var i = 0; i <= g; i++) {
    if (!i) {
      this.points.push(this.makeZeroGenerationPoint(x, y, d));
    } else {
      this.points = this.points.slice().concat(this.rotate(this.points));
    }
  }
};

DragonCurve.prototype.rotate = function (arr) {
  // rotate -90 degree
  var dx = arr[arr.length - 1][0];
  var dy = arr[arr.length - 1][1];

  arr.pop();

  return arr.map(function (p, i, arr) {
      return [-arr[arr.length - 1 - i][1] + dy + dx, arr[arr.length - 1 - i][0] - dx + dy];
  });
};

var result = 0;
var d, curves = {};
var fs = require('fs');
var input = fs.readFileSync('/dev/stdin').toString().split('\n');

input.shift();

input = input.map(function (io) {
    return io.split(' ').map(function (v) {
        return parseInt(v);
    });    
});

input.forEach(function (input) {
  d = new DragonCurve(input[0], input[1], input[2], input[3]);
  d.points.forEach(function (point) {
    curves[point[0] + ',' + point[1]] = [point[0], point[1]];
  });
});

for (var p in curves) {
  if (hasSquare(curves, curves[p])) {
    result++;
  }
}

function hasSquare (curves, point) {
  var x, y, result = true;
  var dx = [0, 1, 0, 1];
  var dy = [0, 0, -1, -1];

  for (var i = 0; i < dx.length; i++) {
    x = point[0] + dx[i];
    y = point[1] + dy[i];
    
    if (!curves.hasOwnProperty(x + ',' + y)) {
      result = false;
      break;
    }
  }

  return result;
}

console.log(result);

*/

/* 2등코드
const stdin = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : __dirname + "/../input.txt")
  .toString()
  .trim()
  .split("\n");
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = +input();
const board = Array.from({ length: 101 }, () => Array(101).fill(false));

let dx = [1, 0, -1, 0];
let dy = [0, -1, 0, 1];

for (let i = 0; i < N; i++) {
  let [x, y, d, g] = input().split(" ").map(Number);
  board[y][x] = true;
  let curve = [d];
  for (let j = 0; j < g; j++) {
    for (let k = curve.length - 1; k >= 0; k--) {
      curve.push((curve[k] + 1) % 4);
    }
  }
  for (let j = 0; j < curve.length; j++) {
    x += dx[curve[j]];
    y += dy[curve[j]];
    if (x < 0 || x > 100 || y < 0 || y > 100) continue;
    board[y][x] = true;
  }
}

let answer = 0;
for (let y = 0; y < 100; y++) {
  for (let x = 0; x < 100; x++) {
    if (board[y][x] && board[y + 1][x] && board[y][x + 1] && board[y + 1][x + 1]) answer++;
  }
}

console.log(answer);
*/
