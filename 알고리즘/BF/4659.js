let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs
  .readFileSync("test.txt")
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const moList = ["a", "e", "i", "o", "u"];

let moCount = 0;
let jaCount = 0;
let prevWord = null;

const init = () => {
  moCount = 0;
  jaCount = 0;
  prevWord = null;
};

for (const word of input) {
  if (word === "end") break;

  init();

  for (const char of word) {
    if (!prevWord) { // char가 첫 번째 인덱스일 경우
      prevWord = char;

      if (moList.includes(char)) {
        moCount += 1;
        jaCount = 0;
      } else {
        moCount = 0;
        jaCount += 1;
      }
    } else {
      if (prevWord === char) {
        if (prevWord == 'e' || prevWord == 'o') {
          moCount += 1;
        } else {
          console.log(`<${word}}> is not acceptable`)
          break;
        }

        if (moList.includes(char)) {
          
        }
      }
    }
  }
}
