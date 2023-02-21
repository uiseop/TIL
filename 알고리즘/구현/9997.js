let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs
    .readFileSync("test.txt")
    .toString()
    .trim()
    .split("\n")
    .map((str) => str.replace("\r", ""));

const [n, ...words] = input;

let answer = 0;
const alphabet = (1 << 26) - 1;

for (let i=0; i<n; i++) {
    let bit_word
    for (let j=0; j<words[i].length; j++) {
        bit_word |= 1 << (words[i].charCodeAt(j) - 97)
    }
    words[i] = bit_word
}

const makeWord = (idx, w) => {
    if (idx === Number(n)) {
        if (w === alphabet) {
            answer += 1;
        }
        return;
    }

    makeWord(idx + 1, w | words[idx]);
    makeWord(idx + 1, w);
};

makeWord(0, 0);

console.log(answer);
