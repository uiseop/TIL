let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const [N, T] = input[0].split(" ").map(Number);

const study = input.slice(1).map((line) => line.split(" ").map(Number));

// const dp = new Array(N+1).fill(null).map((_) => new Array(T+1).fill(0));

// for (let i=1; i<N+1; i++) {
//   for (let j=0; j<=T; j++) {
//     const [K, S] = study[i-1];

//     if (K > j) {
//       dp[i][j] = dp[i-1][j]
//     } else {
//       dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-K] + S)
//     }
//   }
// }

// console.log(dp[N][T]);

const dp = new Array(T+1).fill(0);

for (const [K,S] of study) {
  for (let i=T; i>=K; i--) {
    dp[i] = Math.max(dp[i], dp[i-K] + S)
  }
}

console.log(dp[T]);