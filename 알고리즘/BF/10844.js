let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const N = +input[0];

const burgers = input[1].split(" ").map(Number);

const total = burgers.reduce((acc, cur) => acc + cur, 0);

const dp = Array(total + 1)
  .fill(null)
  .map((_) => Array(total + 1).fill(false));

dp[0][0] = true;

for (let i = 0; i < N; i++) {
  const burger = burgers[i];
  for (let x = total; x >= 0; x--) {
    for (let y = total; y >= 0; y--) {
      if (x - burger >= 0) {
        dp[x][y] |= dp[x - burger][y];
      }
      if (y - burger >= 0) {
        dp[x][y] |= dp[x][y - burger];
      }
    }
  }
}

let answer = 0;

for (let x = 0; x <= total; x++) {
  for (let y = 0; y <= x; y++) {
    const seniorSum = x + y;
    const gilWon = total - seniorSum;
    if (dp[x][y] && y >= gilWon) {
      answer = Math.max(answer, gilWon);
    }
  }
}

console.log(answer);
