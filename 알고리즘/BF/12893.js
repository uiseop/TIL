let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const [N, M] = input[0].split(" ").map(Number);

const parent = new Array(N + 1).fill(null).map((_, idx) => idx);
const enemy = new Array(N + 1).fill(null);

function union(a, b) {
  const pa = find(a);
  const pb = find(b);

  if (pa < pb) {
    parent[pb] = pa;
  } else {
    parent[pa] = pb;
  }
}

function find(a) {
  if (a === parent[a]) return a;

  const pa = find(parent[a]);
  parent[a] = pa;

  return pa;
}

let answer = 1;

for (let i = 1; i < input.length; i++) {
  const [a, b] = input[i].split(" ").map(Number);

  if (find(a) === find(b)) {
    // 둘은 친구관계야
    answer = 0;
    break;
  } else {
    const aEnemy = enemy[a];
    const bEnemy = enemy[b];

    if (!aEnemy) {
      enemy[a] = b;
    } else {
      union(aEnemy, b); // 적의 적은 동료
    }

    if (!bEnemy) {
      enemy[b] = a;
    } else {
      union(bEnemy, a); // 적의 적은 동료
    }
  }
}

console.log(answer);
