let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n").map((str) => str.replace('\r', ''));

const [len, a] = input

const arr = a.split(' ').map((num) => Number(num))

const dp = new Array(Number(len)).fill(null).map((_, idx) => [arr[idx], arr[idx]])

let max_val = 0

for (let i=1; i<len; i++) {
    const temp = dp[i][0]
    for (let j=0; j<i; j++) {
        if (dp[i][1] > dp[j][1] && dp[i][0] < temp + dp[j][0]) {
            dp[i][0] = temp + dp[j][0]
            max_val = max_val < dp[i][0] ? dp[i][0] : max_val
        }
    }
}

console.log(max_val !== 0 ? max_val : arr[0])