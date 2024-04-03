const main = () => {
  const fs = require("fs");
  let input = fs.readFileSync("input.txt").toString().trim().split("\n");
  //let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
  const N = +input[0];
  const lst = input[2].split(" ").map(Number);
  const vst = new Array(101).fill(0);
  const photo = [];
  let cnt = 0;

  lst.forEach((e) => {
    if (vst[e] !== 0) vst[e] += 1;
    else if (cnt < N) {
      photo.push(e);
      vst[e] += 1;
      cnt += 1;
    } else {
      let mn = 1000;
      let mn_i = 0;
      photo.map((n, i) => {
        if (n !== null && mn > vst[n]) {
          mn_i = i;
          mn = vst[n];
        }
      });
      photo.push(e);
      vst[e] += 1;
      vst[photo[mn_i]] = 0;
      photo.splice(mn_i, 1);
    }
  });
  console.log(...photo.sort((a, b) => a - b));
  return;
};

main();


/*
1등 코드
let [N, R, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

N = Number(N)
R = Number(R)
let students = new Array(101).fill(0)   // 추천수 기록
let recommend = []  // 사진틀
const numbers = input[0].split(' ').map(Number)


for(let i=0; i<numbers.length; i++){
    const num = numbers[i];
    if(recommend.includes(num)){
        students[num] += 1;
    }else{
        if(recommend.length < N){   // 사진틀이 비어있을 경우
            recommend.push(num);
            students[num] += 1;
        }else{  // 사진틀이 꽉찼을 경우
            let min_recommend = (1/0);
            let del_student = 0;
            let del_idx = 0;
            for(let k=0; k<recommend.length; k++){
                let temp = min_recommend;
                min_recommend = Math.min(students[recommend[k]], min_recommend);
                if(temp !== min_recommend){ // 최솟값이 변경됐을 경우
                    del_student = recommend[k];
                    del_idx = k;
                }
            }
            students[del_student] = 0;
            recommend.splice(del_idx, 1);
            
            recommend.push(num);
            students[num] += 1;
        }
    }
}

recommend.sort(function(a, b){
    return a - b
});

console.log(recommend.join(' '));
*/
