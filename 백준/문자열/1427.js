let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim().split("");

// console.log(input);
input.sort((a, b) => b - a);
console.log(input.join(""));
