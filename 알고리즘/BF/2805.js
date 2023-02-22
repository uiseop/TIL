let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs
    .readFileSync("test.txt")
    .toString()
    .trim()
    .split("\n")
    .map((str) => str.replace("\r", ""));

const [N, M] = input[0].split(" ").map(Number);

const trees = input[1].split(" ").map(Number);

let start = 0;
let end = trees.reduce((acc, cur) => (acc < cur ? cur : acc));

while (start <= end) {
    console.log('start, end', start, end)
    let mid = Math.floor((start + end) / 2);
    const total = trees.reduce((acc, cur) => {
        const get = cur - mid;
        if (get <= 0) return acc;
        return acc + get;
    }, 0);

    if (total >= M) {
        start = mid + 1;
    } else {
        end = mid - 1;
    }
}

console.log(end);
