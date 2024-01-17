let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const [R, C] = input[0].split(" ").map(Number);

const forest = input.slice(1).map((strs) => strs.split(""));

const END = "D";
const WATER = "*";
const ROCK = "X";
const START = "S";
const WATER_BLOCKS = [END, WATER, ROCK].join("");
const BLOCKS = [WATER, ROCK].join("");

const directions = [
  [-1, 0],
  [1, 0],
  [0, 1],
  [0, -1],
];

function isInRange(r, c) {
  if (0 <= r && r < R && 0 <= c && c < C) return true;
  return false;
}

class Queue {
  constructor() {
    this.items = [];
    this.head = 0;
    this.tail = 0;
  }

  isEmpty() {
    return this.head === this.tail;
  }

  push(value) {
    this.items.push(value);
    this.tail += 1;
  }

  popleft() {
    if (this.isEmpty()) return null;
    return this.items[this.head++];
  }
}

let curR = null;
let curC = null;

let water = new Queue();

for (let r = 0; r < R; r++) {
  for (let c = 0; c < C; c++) {
    if (forest[r][c] === START) {
      curR = r;
      curC = c;
    }

    if (forest[r][c] === WATER) {
      water.push([r, c]);
    }
  }
}

function waterFall() {
  const newWater = new Queue();

  while (!water.isEmpty()) {
    const [r, c] = water.popleft();

    for (const [dr, dc] of directions) {
      const nr = r + dr;
      const nc = c + dc;

      if (isInRange(nr, nc) && !WATER_BLOCKS.includes(forest[nr][nc])) {
        forest[nr][nc] = WATER;
        newWater.push([nr, nc]);
      }
    }
  }

  water = newWater;
}

function move() {
  const newQ = new Queue();

  while (!q.isEmpty()) {
    const [r, c, count] = q.popleft();

    if (forest[r][c] === END) {
      q = new Queue();
      answer = count;
      return;
    }

    for (const [dr, dc] of directions) {
      const nr = r + dr;
      const nc = c + dc;

      if (
        isInRange(nr, nc) &&
        !visited[nr][nc] &&
        !BLOCKS.includes(forest[nr][nc])
      ) {
        visited[nr][nc] = true;
        newQ.push([nr, nc, count + 1]);
      }
    }
  }

  q = newQ;
}

let q = new Queue();
visited = new Array(R).fill(null).map((_) => new Array(C).fill(false));
visited[curR][curC] = true;

q.push([curR, curC, 0]);

let answer = "KAKTUS";

while (!q.isEmpty()) {
  waterFall();
  move();
}

console.log(answer);
