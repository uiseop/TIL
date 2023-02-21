let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs
    .readFileSync("test.txt")
    .toString()
    .trim()
    .split("\n")
    .map((str) => str.replace("\r", ""));

const lst = input[0].split("");

const result = new Array(lst.length).fill("");

const func = (arr, start) => {
    if (arr.length === 0) return;
    const _min = arr.reduce((min, cur) =>
        min.localeCompare(cur) < 0 ? min : cur
    );
    const idx = arr.findIndex((str) => str === _min);
    result[start + idx] = _min;
    console.log(result.join(""));
    func(arr.slice(idx + 1), start + idx + 1);
    func(arr.slice(0, idx), start);
};

func(lst, 0);
