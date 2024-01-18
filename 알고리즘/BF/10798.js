let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let input = fs
  .readFileSync("test.txt")
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const words = input;

const maxLenWord = words.reduce((result, cur) => {
  return result.length > cur.length ? result : cur;
}, "");

const maxLength = maxLenWord.length

let result = "";

for (let i = 0; i < maxLength; i++) {
  for (let j = 0; j < words.length; j++) {
    result += words[j][i] || "";
  }
}

console.log(result);
