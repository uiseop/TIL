let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const [R, C] = input[0].split(" ").map(Number);

const ground = [];

for (let i = 1; i < input.length; i++) {
  ground.push(input[i].split(""));
}

const visited = new Array(R).fill(null).map((_) => new Array(C).fill(false));

const WOLF = "v";
const SHEEP = "k";
const WALL = "#";
const EMPTY = ".";

const DIR = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

function isInRange(r, c) {
  if (0 <= r && r < R && 0 <= c && c < C) return true;
  return false;
}

function isPossibleMove(r, c) {
  if (visited[r][c]) return false;

  const cur = ground[r][c];
  if (cur === WOLF || cur === SHEEP || cur === EMPTY) return true;
  return false;
}

const answer = [0, 0];

for (let r = 0; r < R; r++) {
  for (let c = 0; c < C; c++) {
    if (visited[r][c]) continue;
    if (ground[r][c] === WOLF || ground[r][c] === SHEEP) {
      visited[r][c] = true;

      let vCount = ground[r][c] === WOLF ? 1 : 0;
      let kCount = ground[r][c] === SHEEP ? 1 : 0;
      const q = [];
      q.push([r, c]);

      while (q.length) {
        const [r, c] = q.shift();
        for (const [dr, dc] of DIR) {
          const nr = dr + r;
          const nc = dc + c;

          if (isInRange(nr, nc) && isPossibleMove(nr, nc)) {
            visited[nr][nc] = true;
            if (ground[nr][nc] === WOLF) vCount += 1;
            else if (ground[nr][nc] === SHEEP) kCount += 1;
            q.push([nr, nc]);
          }
        }
      }

      if (kCount > vCount) {
        answer[0] += kCount;
      } else {
        answer[1] += vCount;
      }
    }
  }
}

console.log(answer.join(" "));
