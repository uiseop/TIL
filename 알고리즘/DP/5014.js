let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

class Queue {
  constructor() {
    this.items = [];
    this.head = 0;
    this.tail = 0;
  }

  isEmpty() {
    return this.head === this.tail;
  }

  push(num) {
    this.items.push(num);
    this.tail += 1;
  }

  pop() {
    if (this.isEmpty()) return null;
    return this.items[this.head++];
  }
}

const FAIL = "use the stairs";

const [F, S, G, U, D] = input[0].split(" ").map(Number);

const DP = Array(F + 1).fill(Infinity);

DP[S] = 0;

const q = new Queue();

q.push(S);

function isInRange(cur) {
  if (0 < cur && cur <= F) return true;
  return false;
}

while (!q.isEmpty()) {
  const cur = q.pop();

  for (const gap of [U, -D]) {
    const next = cur + gap;
    if (isInRange(next)) {
      if (DP[next] > DP[cur] + 1) {
        DP[next] = DP[cur] + 1;
        q.push(next);
      }
    }
  }
}

console.log(DP[G] === Infinity ? FAIL : DP[G]);
