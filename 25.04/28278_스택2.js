let fs = require("fs");

let input = fs
  .readFileSync("./input.txt") // .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let N = +input[0];
let stk = [];
let result = [];

const op1 = (i) => {
  i = i.split(" ");
  stk.push(+i[1]);
  return;
};

const op2 = () => {
  if (stk.length) result.push(stk.pop());
  else result.push(-1);
  return;
};
const op3 = () => {
  result.push(stk.length);
  return;
};
const op4 = () => {
  if (!stk.length) result.push(1);
  else result.push(0);
  return;
};
const op5 = () => {
  const len = stk.length;
  if (len) result.push(stk[len - 1]);
  else result.push(-1);
  return;
};

for (let i = 1; i < N + 1; i++) {
  let now = input[i];
  if (now.startsWith("1")) op1(now);
  else if (now == "2") op2();
  else if (now == "3") op3();
  else if (now == "4") op4();
  else if (now == "5") op5();
}

console.log(result.join("\n"));

process.exit();

/*
1등 코드 (ㄷㄷㄷㄷ)


function Solver(stdlib, foreign, heap) {
  'use asm';
  var print = foreign.print, read = foreign.read, heap8 = new stdlib.Uint8Array(heap), heap32 = new stdlib.Uint32Array(heap), floor = stdlib.Math.floor, imul = stdlib.Math.imul, input = 0, input_end = 0, output = 65536, output_end = 65536, stack = 131072;
  function run() {
    var N = 0, x = 0, arr = 0, i = 0, top = 0, op = 0;
    N = ru() | 0;
    arr = stack | 0;
    stack = (stack + 4000000) | 0;
    for (; (i | 0) < (N | 0); i = (i + 1) | 0) {
      white();
      if ((input | 0) == (input_end | 0)) fill();
      op = heap8[input | 0] | 0;
      input = (input + 1) | 0;
      if ((op | 0) == 49) {
        heap32[(arr + top) >> 2] = ru() | 0;
        top = (top + 4) | 0;
        continue;
      } else if ((op | 0) == 50) {
        if (top | 0) {
          top = (top - 4) | 0;
          pu(heap32[(arr + top) >> 2] | 0);
        } else {
          pc(45);
          pc(49);
        }
      } else if ((op | 0) == 51) {
        pu(top >> 2);
      } else if ((op | 0) == 52) {
        pc(48 | ((top | 0) == 0));
      } else {
        if (top | 0) {
          pu(heap32[(arr + top - 4) >> 2] | 0);
        } else {
          pc(45);
          pc(49);
        }
      }
      pc(10);
    }
    flush();
  }
  function fill() {
    input_end = read(output | 0) | 0;
    input = 0;
  }
  function flush() {
    print(output | 0, output_end | 0);
    output_end = output | 0;
  }
  function white() {
    var i = 0;
    while (1) {
      for (i = (input | 0); (i | 0) < (input_end | 0); i = (i + 1) | 0) {
        if ((heap8[i | 0] | 0) > 32) {
          input = i | 0;
          return;
        }
      }
      fill();
    }
  }
  function ru() {
    var x = 0, i = 0, c = 0;
    white();
    while (1) {
      for (i = (input | 0); (i | 0) < (input_end | 0); i = (i + 1) | 0) {
        c = heap8[i | 0] | 0;
        if ((c | 0) < 48 | (c | 0) > 58) {
          input = i | 0;
          return x | 0;
        }
        x = (imul(x, 10) + c - 48) | 0;
      }
      fill();
    }
    return 0;
  }
  function ri() {
    var x = 0, i = 0, c = 0, s = 1;
    white();
    if ((input | 0) == (input_end | 0)) fill();
    if ((heap8[input | 0] | 0) == 45) {
      s = -1;
      input = (input + 1) | 0;
    }
    while (1) {
      for (i = (input | 0); (i | 0) < (input_end | 0); i = (i + 1) | 0) {
        c = heap8[i | 0] | 0;
        if ((c | 0) < 48 | (c | 0) > 58) {
          input = i | 0;
          return imul(x | 0, s | 0);
        }
        x = (imul(x, 10) + c - 48) | 0;
      }
      fill();
    }
    return 0;
  }
  function pc(x) {
    x = x | 0;
    if (((output_end + 1) | 0) > 131072) flush();
    heap8[output_end | 0] = x | 0;
    output_end = (output_end + 1) | 0;
  }
  function pu(x) {
    x = x | 0;
    var len = 16, i = 0;
    if (((output_end + 16) | 0) > 131072) flush();
    do {
      len = (len - 1) | 0;
      heap8[(stack + len) | 0] = ((x | 0) % 10 + 48) | 0;
      x = ((x | 0) / 10) | 0;
    } while ((x | 0) > 0);
    for (i = 0; ((i + len) | 0) < 16; i = (i + 1) | 0) {
      heap8[(output_end + i) | 0] = heap8[(stack + len + i) | 0] | 0;
    }
    output_end = (output_end + 16 - len) | 0;
  }
  function pi(x) {
    x = x | 0;
    if (((output_end + 1) | 0) > 131072) flush();
    if ((x | 0) < 0) {
      heap8[output_end | 0] = 45;
      output_end = (output_end + 1) | 0;
      x = (-x) | 0;
    }
    pu(x | 0);
  }
  return {
    run: run,
  };
}

const { readSync, writeSync } = require('fs');
const heap = new Uint8Array(1 << 24);
const solver = Solver(global, {
  read(len) {
    const r = readSync(0, heap, 0, len);
    if (r === 0) process.exit(0);
    return r;
  },
  print(pos, end) {
    writeSync(1, heap, pos, end - pos);
  }
}, heap.buffer);
solver.run()

*/
