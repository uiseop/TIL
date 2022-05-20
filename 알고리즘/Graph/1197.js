let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n");

function PrioQ() {
    this.items = []; // 포화 이진 트리 -> 배열로 가능
}

PrioQ.prototype.swap = function (id, pid) {
    const temp = this.items[pid];
    this.items[pid] = this.items[id];
    this.items[id] = temp;
};

PrioQ.prototype.parentIndex = function (id) {
    return Math.floor((id - 1) / 2);
};

PrioQ.prototype.parent = function (id) {
    return this.items[this.parentIndex(id)];
};

PrioQ.prototype.heappush = function (edges) {
    const [v, w] = edges;
    this.items.push([v, w]);
    let id = this.items.length - 1;
    while (this.parent(id) && this.parent(id)[1] > w) {
        const pid = this.parentIndex(id);
        this.swap(id, pid);
        id = pid;
    }
};

PrioQ.prototype.leftChildIndex = function (id) {
    return 2 * id + 1;
};

PrioQ.prototype.leftChild = function (id) {
    return this.items[this.leftChildIndex(id)];
};

PrioQ.prototype.rightChildIndex = function (id) {
    return 2 * id + 2;
};

PrioQ.prototype.rightChild = function (id) {
    return this.items[this.rightChildIndex(id)];
};

PrioQ.prototype.heappop = function () {
    if (this.items.length === 1) {
        return this.items.pop();
    }
    this.swap(0, this.items.length - 1);
    const result = this.items.pop();
    let id = 0;
    const w = this.items[0][1];
    while (
        (this.leftChild(id) && this.leftChild(id)[1] < w) ||
        (this.rightChild(id) && this.rightChild(id)[1] < w)
    ) {
        let cid = this.leftChildIndex(id);
        if (this.rightChild(id) && this.rightChild(id)[1] < w) {
            cid = this.rightChildIndex(id);
        }
        this.swap(id, cid);
        id = cid;
    }
    return result;
};

function Graph() {
    this.items = {};
}

Graph.prototype.addVertex = function (v) {
    this.items[v] = {};
};

Graph.prototype.addEdge = function (v1, v2, w) {
    this.items[v1][v2] = w;
    this.items[v2][v1] = w;
};

const [v, e] = input[0].split(" ").map((num) => parseInt(num));
const q = new PrioQ();
const graph = new Graph();

for (let i = 1; i <= v; i++) {
    graph.addVertex(i);
}

for (let i = 1; i < input.length; i++) {
    const [v1, v2, w] = input[i].split(" ").map((num) => parseInt(num));
    graph.addEdge(v1, v2, w);
}

const distance = {};
for (let i = 1; i <= v; i++) {
    distance[i] = Number.POSITIVE_INFINITY;
}

distance[1] = 0;

q.heappush([1, 0]);

let result = 0;
let count = 0;

const visited = new Array(v + 1).fill(false);

while (q.items.length !== 0) {
    // PrioQ { items: [ [ '1', 0 ], [ '2', Infinity ], [ '3', Infinity ] ] } Graph { items: { '1': { '2': 1, '3': 3 }, '2': { '3': 22 }, '3': {} } }
    const [vertex, weight] = q.heappop();
    if (visited[vertex]) continue;
    visited[vertex] = true;
    result += weight;
    if(++count === v) {
        break;
    }
    for (let [v, w] of Object.entries(graph.items[vertex])) {
        console.log(v,w)
        q.heappush([v, w]);
    }
    console.log(`q is ${q.items.map((arr) => arr[1])}`)
}
console.log(result);
