const solve = () => {
  let fs = require("fs");
  let input = fs.readFileSync("input.txt").toString().split("\n");
  // let input = fs.readFileSync('/dev/stdin').toString().split('\n');
  input = input.map((e, idx) => e.split(" ").map((e) => +e));

  const [V, E] = input.shift();
  const arr = input.sort((a, b) => a[2] - b[2]);
  const parrent = new Array(V).fill(0).map((e, idx) => idx);
  let [cnt, cost] = [0, 0];

  const get_parrent = (idx) => {
    if (parrent[idx] !== idx) return get_parrent(parrent[idx]);
    else return idx;
  };

  const union = (v1, v2) => {
    const [a, b] = [get_parrent(v1), get_parrent(v2)];
    if (a === b) return false;
    if (a > b) parrent[a] = b;
    else parrent[b] = a;
    return true;
  };

  for (let [v1, v2, n] of arr) {
    if (cnt === V - 2) break;
    if (union(v1, v2)) {
      cnt = cnt + 1;
      cost = cost + n;
    }
  }

  console.log(cost);
  return;
};

solve();
