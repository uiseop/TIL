let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs
//     .readFileSync("test.txt")
//     .toString()
//     .trim()
//     .split("\n")
//     .map((str) => str.replace("\r", ""));

const N = Number(input[0]);
const board = input.slice(1).map((str) => str.split(""));
let result = 0;

const findLongestLine = (arr) => {
    let result = 1;

    for (let r = 0; r < N; r++) {
        let temp = 1;
        for (let c = 1; c < N; c++) {
            if (arr[r][c - 1] === arr[r][c]) {
                temp += 1;
            } else {
                result = Math.max(result, temp);
                temp = 1;
            }
        }
        result = Math.max(result, temp);
    }

    for (let c = 0; c < N; c++) {
        let temp = 1;
        for (let r = 1; r < N; r++) {
            if (arr[r - 1][c] === arr[r][c]) {
                temp += 1;
            } else {
                result = Math.max(result, temp);
                temp = 1;
            }
        }
        result = Math.max(result, temp);
    }

    return result;
};

const switchItem = (arr, r, c, nr, nc) => {
    const temp = arr[r][c];
    arr[r][c] = arr[nr][nc];
    arr[nr][nc] = temp;
};

result = Math.max(result, findLongestLine(board));

const dr = [0, 1];
const dc = [1, 0];

for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
        for (let k = 0; k < 2; k++) {
            if (r + dr[k] < N && c + dc[k] < N) {
                const nr = r + dr[k];
                const nc = c + dc[k];
                switchItem(board, r, c, nr, nc);
                result = Math.max(result, findLongestLine(board));
                switchItem(board, r, c, nr, nc);
            }
        }
    }
}

console.log(result);
