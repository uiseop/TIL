let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim().split("");

// console.log(input); 파일 내용안에 있는 내용은 Array형식으로 들어온다

input.sort((a, b) => b - a);
console.log(input.join(""));
