let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n");

function Graph() {
    this.items = {};
}

Graph.prototype.addVertex = function (v) {
    this.items[v] = {};
};

Graph.prototype.addEdges = function (edge) {
    const [v1, v2, w] = edge;
    if (this.items[v1][v2] && this.items[v1][v2] < w) {
        return;
    }
    this.items[v1][v2] = w;
};

function PrioQ() {
    this.items = [];
}

PrioQ.prototype.parentIndex = function (idx) {
    return Math.floor((idx - 1) / 2);
};

PrioQ.prototype.parent = function (idx) {
    return this.items[this.parentIndex(idx)];
};

PrioQ.prototype.swap = function (idx, pid) {
    const temp = this.items[pid];
    this.items[pid] = this.items[idx];
    this.items[idx] = temp;
};

PrioQ.prototype.heappush = function (v, w) {
    this.items.push([v, w]);
    let idx = this.items.length - 1;
    while (this.parent(idx) && this.parent(idx)[1] > w) {
        let pid = this.parentIndex(idx);
        this.swap(idx, pid);
        idx = pid;
    }
};

PrioQ.prototype.leftChild = function (idx) {
    return this.items[this.leftChildIndex(idx)];
};

PrioQ.prototype.leftChildIndex = function (idx) {
    return 2 * idx + 1;
};
PrioQ.prototype.rightChild = function (idx) {
    return this.items[this.rightChildIndex(idx)];
};

PrioQ.prototype.rightChildIndex = function (idx) {
    return 2 * idx + 2;
};

PrioQ.prototype.heappop = function () {
    if (this.items.length === 1) {
        return this.items.pop();
    }
    let idx = 0;
    this.swap(idx, this.items.length - 1);
    const result = this.items.pop();
    const w = this.items[0][1];
    while (
        (this.leftChild(idx) && this.leftChild(idx)[1] < w) ||
        (this.rightChild(idx) && this.rightChild(idx)[1] < w)
    ) {
        let cid = this.leftChildIndex(idx);
        if (
            this.rightChild(idx) &&
            this.rightChild(idx)[1] < this.leftChild(idx)[1]
        ) {
            cid = this.rightChildIndex(idx);
        }
        this.swap(idx, cid);
        idx = cid;
    }
    return result;
};

PrioQ.prototype.dijkstra = function (input) {
    const n = parseInt(input[0]);
    const m = parseInt(input[1]);
    const graph = new Graph();
    const distance = {}

    for (let i = 1; i <= n; i++) {
        graph.addVertex(i);
        distance[i] = Number.POSITIVE_INFINITY
    }

    for (let i = 2; i < input.length - 1; i++) {
        graph.addEdges(input[i].split(" ").map((num) => parseInt(num)));
    }

    const [start, end] = input[input.length - 1]
        .split(" ")
        .map((num) => parseInt(num));
    
    distance[start] = 0;

    this.heappush(start, 0);
    while (this.items.length !== 0) {
        const [current_v, current_w] = this.heappop();
        for (let [next_v, next_w] of Object.entries(graph.items[current_v])) {
            if (distance[next_v] > current_w + next_w) {
                const new_w = current_w + next_w;
                distance[next_v] = new_w;
                this.heappush(next_v, new_w);
            }
        }
    }
    return distance[end]
};

const q = new PrioQ();
console.log(q.dijkstra(input));
