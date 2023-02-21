let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n").map((str) => str.replace('\r', ''));

const [len, a] = input

const arr = a.split(' ').map((num) => Number(num))

const dp = new Array(Number(len)).fill(null).map((_, idx) => [arr[idx], 1])

let max_val = 1

for (let i=len-1; i>-1; i--) {
    for (let j=len-1; j>i; j--) {
        if (arr[i] > arr[j] && dp[i][1] < 1 + dp[j][1]) {
            dp[i][1] += 1
            max_val = max_val < dp[i][1] ? dp[i][1] : max_val
        }
    }
}

console.log(max_val !== 0 ? max_val : arr[0])