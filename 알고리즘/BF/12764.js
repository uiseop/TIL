let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const N = +input[0];

const timeLog = [];

for (let i = 1; i <= N; i++) {
  timeLog.push(input[i].split(" ").map(Number));
}

timeLog.sort((a, b) => {
  if (a[0] === b[0]) {
    return a[1] - b[1];
  }
  return a[0] - b[0];
});

class Heap {
  constructor() {
    this.items = [];
  }

  size() {
    return this.items.length;
  }

  getPid(id) {
    return Math.floor((id - 1) / 2);
  }

  getLid(id) {
    return 2 * id + 1;
  }

  getRid(id) {
    return 2 * id + 2;
  }

  swap(id1, id2) {
    [this.items[id1], this.items[id2]] = [this.items[id2], this.items[id1]];
  }

  heappush(value) {
    let id = this.items.length;

    this.items.push(value);

    while (id) {
      const pid = this.getPid(id);

      if (this.items[pid].key > value.key) {
        this.swap(pid, id);

        id = pid;
      } else {
        return;
      }
    }
  }

  pop() {
    if (this.items.length === 0) return null;

    this.swap(0, this.items.length - 1);

    const result = this.items.pop();

    let id = 0;
    const value = this.items[id];
    let lid = this.getLid(id);
    let rid = this.getRid(id);

    while (
      (this.items[lid] && value.key > this.items[lid].key) ||
      (this.items[rid] && value.key > this.items[rid].key)
    ) {
      let cid = lid;

      if (this.items[rid] && this.items[lid].key > this.items[rid].key) {
        cid = rid;
      }

      this.swap(id, cid);
      id = cid;

      lid = this.getLid(id);
      rid = this.getRid(id);
    }

    return result;
  }
}

let left = 1;
let right = N - 1;
let answer = [Infinity, 0];

while (left <= right) {
  mid = Math.floor((left + right) / 2);

  const flag = isPossible(mid);

  if (flag) {
    right = mid - 1;
    if (answer[0] > mid) {
      answer = [mid, flag];
    }
  } else {
    left = mid + 1;
  }
}

function isPossible(x) {
  const cidHeap = new Heap();
  const timeHeap = new Heap();
  const count = new Array(x).fill(0);

  let i = 0;

  for (let i = 0; i < x; i++) {
    cidHeap.heappush({ key: i });
  }

  while (true) {
    while (
      timeLog[i] &&
      timeHeap.items[0] &&
      timeLog[i][0] >= timeHeap.items[0].key
    ) {
      // 좌석 반납
      const poped = timeHeap.pop();
      cidHeap.heappush({ key: poped.cid });
    }

    const cidObj = cidHeap.pop();

    if (!cidObj) return false;

    timeHeap.heappush({ key: timeLog[i++][1], cid: cidObj.key }); // 좌석 배정
    count[cidObj.key] += 1;

    if (i === N) return count.join(" "); // true로 처리됨
  }
}

console.log(answer.join("\n"));
