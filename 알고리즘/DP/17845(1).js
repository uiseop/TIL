let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const [N, K] = input[0].split(" ").map(Number);

const courseList = [];

for (let i = 1; i <= K; i++) {
  courseList.push(input[i].split(" ").map(Number));
}

const DP = Array(N + 1).fill(0);

let answer = 0;

for (const [I, T] of courseList) {
  for (let i = N; i >= T; i--) {
    DP[i] = Math.max(DP[i], DP[i - T] + I);
  }
}

console.log(answer, DP);
