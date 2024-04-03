let fs = require("fs");
let input = fs.readFileSync("input.txt").toString().split('\n');
// let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let cnt = 0;
let arr = new Array(31).fill(0);
let ans = []

input.map((num)=> { arr[num] += 1 })

for (let i = 1; i< 32; i++){
    const e = arr[i]
    if (!e){
        cnt += 1; ans.push(i);
    }
    if (cnt === 2) break;
}

console.log(ans[0]);
console.log(ans[1]);
