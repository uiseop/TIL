let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n");

function Graph() {
    this.edges = {};
}

Graph.prototype.addVertex = function(v) {
    this.edges[v] = {};
}

Graph.prototype.addEdge = function (v1,v2,w) {
    this.edges[v1][v2] = w;
}

Graph.prototype.union = function (v1,v2,parents) {
    const x = this.find(v1, parents);
    const y = this.find(v2, parents);
    if (x !== y) {
        parents[y] = x;
    }
}

Graph.prototype.find = function (v, parents) {
    if (v === parents[v]) return v;
    // const y = this.find(parents[v], parents);
    // parents[v] = y;
    // return y;
    return parents[v] = this.find(parents[v], parents)
}

Graph.prototype.kruskal = function() {
    const heap = new Heap();
    const parents = new Array(Object.keys(this.edges).length + 1).fill().map((v,i) => i);
    let total = 0;
    let edges = 0;
    const length = Object.keys(this.edges).length;
    for (let from in this.edges) {
        for (let [to, weight] of Object.entries(this.edges[from])) {
            heap.heappush(from, to, weight)
        }
    }
    while (length - 1 !== edges) {
        const [v1, v2, w] = heap.heappop().map((num) => parseInt(num));
        if (this.find(v1, parents) !== this.find(v2, parents)) {
            this.union(v1,v2,parents)
            total += w;
            edges += 1;
        }
    }
    return total
}

function Heap() {
    this.arr = [];
}

Heap.prototype.getParentIndex = function (idx) {
    return Math.floor((idx-1) / 2)
}

Heap.prototype.getParent = function (idx) {
    return this.arr[this.getParentIndex(idx)]
}

Heap.prototype.getParentWeight = function (idx) {
    return this.arr[this.getParentIndex(idx)][2]
}

Heap.prototype.swap = function (idx, pid) {
    const temp = this.arr[pid];
    this.arr[pid] = this.arr[idx];
    this.arr[idx] = temp;
}

Heap.prototype.heappush = function (v1, v2, w) {
    this.arr.push([v1, v2, w]);
    let idx = this.arr.length - 1;
    while (this.getParent(idx) && this.getParentWeight(idx) > w) {
        const pid = this.getParentIndex(idx);
        this.swap(idx, pid);
        idx = pid;
    }
}

Heap.prototype.leftChildIndex = function (idx) {
    return 2*idx + 1;
}

Heap.prototype.leftChild = function (idx) {
    return this.arr[this.leftChildIndex(idx)]
}

Heap.prototype.leftChildWeight = function (idx) {
    return this.leftChild(idx)[2]
}

Heap.prototype.rightChildIndex = function (idx) {
    return 2*idx + 2;
}

Heap.prototype.rightChild = function (idx) {
    return this.arr[this.rightChildIndex(idx)]
}

Heap.prototype.rightChildWeight = function (idx) {
    return this.rightChild(idx)[2]
}

Heap.prototype.heappop = function () {
    if (this.arr.length === 1) {
        return this.arr.pop()
    }
    this.swap(0, this.arr.length - 1);
    const result = this.arr.pop();
    let idx = 0;
    const weight = this.arr[idx][2];
    while ((this.leftChild(idx) && this.leftChildWeight(idx) < weight) || (this.rightChild(idx) && this.rightChildWeight(idx) < weight)) {
        let cid = this.leftChildIndex(idx);
        if (this.rightChild(idx) && this.rightChildWeight(idx) < this.leftChildWeight(idx)) {
            cid = this.rightChildIndex(idx);
        }
        this.swap(idx, cid);
        idx = cid;
    }
    return result;
}

const n = parseInt(input[0]);
const m = parseInt(input[1]);

const graph = new Graph();

for(let i=1; i<=n; i++) {
    graph.addVertex(i)
}

for (let i=2; i<input.length; i++) {
    const [v1, v2, w] = input[i].split(" ").map((num) => parseInt(num))
    graph.addEdge(v1, v2, w)
}

/* 
console.log(graph.edges)
{
  '1': { '2': 5, '3': 4 },
  '2': { '3': 2, '4': 7 },
  '3': { '4': 6, '5': 11 },
  '4': { '5': 3, '6': 8 },
  '5': { '6': 8 },
  '6': {}
}


input: 
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
*/

console.log(graph.kruskal())