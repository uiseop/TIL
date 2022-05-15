const { Console } = require("console");
let fs = require("fs")
// let input = fs.readFileSync("/dev/stdin").toString().split("\n")
let input = fs.readFileSync("test.txt").toString().split("\n")

const n = parseInt(input[0])
const m = parseInt(input[1])
const roads = [];

for (let i=2; i<input.length; i++) {
    roads.push(input[i].split(" ").map((num) => parseInt(num)))
}

