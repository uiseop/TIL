let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs
    .readFileSync("test.txt")
    .toString()
    .trim()
    .split("\n")
    .map((str) => Number(str.replace("\r", "")));

const [N, ...rice] = input;

// let left = 0;
// let right = N - 1;

dp = new Array(N).fill(null).map((_) => new Array(N).fill(0));

const get_maxValue = (s, e, cnt) => {
    if (s === e) return cnt * rice[s];
    if (dp[s][e]) return dp[s][e];

    dp[s][e] = Math.max(
        get_maxValue(s + 1, e, cnt + 1) + cnt * rice[s],
        get_maxValue(s, e - 1, cnt + 1) + cnt * rice[e]
    );
    return dp[s][e]
};

console.log(get_maxValue(0, N-1, 1))