let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

function getManhattanDistance(pos1, pos2) {
  const [x1, y1] = pos1;
  const [x2, y2] = pos2;
  return Math.abs(x1 - x2) + Math.abs(y1 - y2);
}

const [N, K] = input.shift().split(" ").map(Number);
const pos = input.map((nums) => nums.split(" ").map(Number));

const distances = new Array(N)
  .fill(null)
  .map((_) => new Array(N).fill(Infinity));

for (let i = 0; i < N; i++) {
  for (let j = i + 1; j < N; j++) {
    const dist = getManhattanDistance(pos[i], pos[j]);
    distances[i][j] = dist;
  }
}

const dp = new Array(K + 1).fill(null).map((_) => new Array(N).fill(Infinity));

dp[0][0] = 0;

for (let i = 1; i < N; i++) {
  dp[0][i] = dp[0][i - 1] + distances[i - 1][i];
}

for (let i = 1; i <= K; i++) {
  for (let j = 1; j < N; j++) {
    // for (let k = i; k > 0; k--) {
    //   if (j - k - 1 < 0) continue;

    //   dp[i][j] = Math.min(
    //     dp[i][j],
    //     dp[i - k][j - k - 1] + distances[j - k - 1][j],
    //     dp[i][j - 1] + distances[j - 1][j]
    //   );
    // }
    if (j <= i) continue
    for (let k = 0; k <= i; k++) {
      dp[i][j] = Math.min(
        dp[i][j],
        dp[i - k][j - k - 1] + distances[j - k - 1][j]
      );
    }
  }
}

console.log(dp[K][N - 1]);
