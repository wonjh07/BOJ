let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split("\n");
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const main = () => {
  const T = +input[0];

  const match = (x, y) => {
    let temp = 0;
    for (let j = 0; j < 4; j++) {
      if (x[j] !== y[j]) temp++;
    }
    return temp;
  };

  for (let i = 0; i < T; i++) {
    const N = +input[i * 2 + 1];

    if (N > 32) {
      console.log(0);
      continue;
    }

    let min = Infinity;
    const mbti = input[i * 2 + 2].split(" ");

    for (let a = 0; a <= N - 3; a++) {
      for (let b = a + 1; b <= N - 2; b++) {
        const now = match(mbti[a], mbti[b]);
        for (let c = b + 1; c <= N - 1; c++) {
          const temp2 = now + match(mbti[a], mbti[c]) + match(mbti[b], mbti[c]);
          if (min > temp2) min = temp2;
        }
      }
    }
    console.log(min);
  }
  return;
};

main();
