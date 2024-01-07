let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

class Heap {
  constructor() {
    this.items = [];
  }

  getPid(id) {
    if (id === 0) return 0;

    return Math.floor((id - 1) / 2);
  }

  getLid(id) {
    return 2 * id + 1;
  }

  getRid(id) {
    return 2 * id + 2;
  }

  swap(cid, pid) {
    [this.items[cid], this.items[pid]] = [this.items[pid], this.items[cid]];
  }

  heappush(value) {
    let cid = this.items.length;
    this.items.push(value);

    let pid = this.getPid(cid);

    while (cid !== 0 && this.items[pid] > value) {
      this.swap(cid, pid);
      cid = pid;
      pid = this.getPid(cid);
    }
  }

  heappop() {
    if (this.items.length === 0) {
      return 0;
    }
    if (this.items.length === 1) {
      return this.items.pop();
    }

    let id = 0;
    this.swap(0, this.items.length - 1);

    const result = this.items.pop();

    let lid, rid, cid;

    lid = this.getLid(id);
    rid = this.getRid(id);

    while (
      (this.items[lid] && this.items[id] > this.items[lid]) ||
      (this.items[rid] && this.items[id] > this.items[rid])
    ) {
      cid = lid;

      if (this.items[rid] && this.items[cid] > this.items[rid]) {
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

const heap = new Heap();

const N = +input[0];

const answer = [];

for (let i = 1; i <= N; i++) {
  const op = +input[i];

  if (op) {
    heap.heappush(op);
  } else {
    answer.push(heap.heappop());
  }
}

console.log(answer.join("\n"));
