let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const N = +input[0];
const Ws = input[1].split(" ").map(Number);

function solution(N, Ws) {
  let answer = 0;
  function backtracking(WList) {
    if (WList.length === 2) return 0;

    let result = 0;

    for (let i = 1; i < WList.length - 1; i++) {
      const curEnergy = WList[i - 1] * WList[i + 1];
      result = Math.max(
        result,
        curEnergy + backtracking([...WList.slice(0, i), ...WList.slice(i + 1)])
      );
    }

    return result;
  }

  answer = Math.max(answer, backtracking(Ws));

  return answer;
}

console.log(solution(N, Ws));
