let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const [N, K, D] = input.shift().split(" ").map(Number);

const rules = input.map((numbers) => numbers.split(" ").map(Number));

let left = 0;
let right = 10 ** 6 + 1;

while (left <= right) {
  mid = Math.floor((left + right) / 2);

  let total = 0;

  for (const [frm, to, gap] of rules) {
    if (frm > mid) continue;

    let end = Math.min(to, mid);
    total += Math.floor((end - frm) / gap) + 1;
  }

  if (total < D) {
    left = mid + 1;
  } else {
    right = mid - 1;
  }
}

console.log(left);
