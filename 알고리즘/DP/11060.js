let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const N = +input[0];

const maze = input[1].split(" ").map(Number);

const DP = new Array(N).fill(Number.MAX_SAFE_INTEGER);
DP[0] = 0;

const q = [];
q.push([0, maze[0]]);

while (q.length) {
  const [curPos, A] = q.shift();

  for (let a = 1; a <= A; a++) {
    if (curPos + a >= N) continue;

    const nextPos = curPos + a;

    if (DP[nextPos] > DP[curPos] + 1) {
      DP[nextPos] = DP[curPos] + 1;

      q.push([nextPos, maze[nextPos]]);
    }
  }
}

console.log(DP.at(-1) === Number.MAX_SAFE_INTEGER ? -1 : DP.at(-1));
