let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const N = Number(input[0]);

const liquids = input[1].split(" ").map(Number);

liquids.sort((a, b) => a - b);

let min = Infinity;
let answer = [];

let left = 0;
let right = N - 1;

while (left < right) {
  let sum = liquids[left] + liquids[right];

  if (sum > 0) {
    if (min > sum) {
      min = sum;
      answer = [left, right]
    }
    right -= 1;
  } else if (sum < 0) {
    if (min > Math.abs(sum)) {
      min = Math.abs(sum);
      answer = [left, right]
    }
    left += 1;
  } else {
    min = 0;
    answer = [left, right]
    break;
  }
}

const [l, r] = answer;

console.log(liquids[l], liquids[r]);
