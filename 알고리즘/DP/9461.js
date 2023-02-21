let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("test.txt").toString().trim().split("\n").map((str) => str.replace('\r', ''));

const [T, ...p] = input.map(Number)

const P = [1,1,1,2,2,3,4,5,7,9]

for (let i=10; i<100; i++) {
    P.push(P[i-1] + P[i-5])
}

for (let pid of p) {
    console.log(P[pid-1])
}