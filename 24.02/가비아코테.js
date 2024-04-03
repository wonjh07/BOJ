const [folders, ...commands] = require("fs")
  .readFileSync("input.txt") // '/dev/stdin'
  .toString()
  .trim()
  .split("\n")
  .map((e) => e.split(","));

let dir = { "C:": {} };
let nowAd = ["C:"];

// 최초 디렉토리 구성
const initDir = (ads) => {
  let tmpNowObj = dir;
  for (let ad of ads) {
    if (!(ad in tmpNowObj)) {
      ad.includes(".") ? (tmpNowObj[ad] = "file") : (tmpNowObj[ad] = {});
    }
    tmpNowObj = tmpNowObj[ad];
  }
  return;
};

// 현재 위치
const dirNow = () => {
  let tmpNowObj = dir;
  for (let d of nowAd) tmpNowObj = tmpNowObj[d];
  return tmpNowObj;
};

// 디렉토리 유효성여부
const validDir = (ads) => {
  let tmpNowObj = dir;
  for (let tg of ads.split("/")) {
    if (!(tg in tmpNowObj)) return false;
    tmpNowObj = tmpNowObj[tg];
  }
  return true;
};

// cd 명령어
const cd = (target) => {
  if (target.includes("C:") && validDir(target)) {
    nowAd = target.split("/");
  } else if (!target.includes("C:") && target in dirNow()) {
    nowAd.push(target);
  }
};

// mkdir 명령어
const mkdir = (target) => {
  if (target.includes("C:")) {
    let tempNow = dir;
    target.split("/").forEach((e) => {
      if (!(e in tempNow)) tempNow[e] = {};
      tempNow = tempNow[e];
    });
  } else if (!target.includes("C:") && !(target in dirNow())) {
    dirNow()[target] = {};
  }
};

// rmvdir 명령어
const rmvdir = (target) => {
  if (target.includes("C:") && validDir(target)) {
    let tempNow = dir;
    const targetSplit = target.split("/");
    for (let i = 0; i < targetSplit.length; i++) {
      if (i === targetSplit.length - 1) {
        delete tempNow[targetSplit[i]];
      }
      tempNow = tempNow[targetSplit[i]];
    }
    // 현재 경로상에 제거된 폴더가 있다면 그 상위폴더로 이동
    if (target.includes(nowAd.join("/"))) {
      targetSplit.pop();
      nowAd = targetSplit;
    }
  } else if (!target.includes("C:") && target in dirNow()) {
    delete dirNow()[target];
  }
};

// main
folders.forEach((e) => initDir(e.split("/")));

for (let command of commands) {
  const [a, b] = command;
  if (a === "cd") cd(b);
  else if (a === "mkdir") mkdir(b);
  else if (a === "rmvdir") rmvdir(b);
}

console.log(dir);
console.log(nowAd);
console.log(dirNow());
