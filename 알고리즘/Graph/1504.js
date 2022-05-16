let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [vertex, edge] = input[0].split(" ").map((num) => parseInt(num));

function Graph() {
    this.edges = {};
}

Graph.prototype.addVertex = function (v) {
    this.edges[v] = {};
};

Graph.prototype.addEdge = function (v1, v2, w) {
    this.edges[v1][v2] = w;
    this.edges[v2][v1] = w;
};

const graph = new Graph();

for (let i = 1; i <= vertex; i++) {
    graph.addVertex(i);
}

for (let i = 1; i < input.length - 1; i++) {
    const [v1, v2, w] = input[i].split(" ").map((num) => parseInt(num));
    graph.addEdge(v1, v2, w);
}

const [v1, v2] = input[input.length-1].split(" ").map((num) => parseInt(num))

function PrioQ() {
    this.heap = [];
}

PrioQ.prototype.swap = function(id, pid) {
    const temp = this.heap[pid];
    this.heap[pid] = this.heap[id];
    this.heap[id] = temp;
}

PrioQ.prototype.getPid = function(id) {
    return Math.floor((id-1) / 2)
}

PrioQ.prototype.pWeight = function(id) {
    return this.heap[this.getPid(id)]
}

PrioQ.prototype.heappush = function (vertex, weight) {
    this.heap.push([vertex, weight]);
    let id = this.heap.length - 1;
    let pid = this.getPid(id);
    while (this.heap[pid] && this.pWeight(id) > weight) {
        this.swap(id, pid);
        id = pid;
        pid = this.getPid(id);
    }
}

PrioQ.prototype.heappop = function () {
    if (this.heap.length === 1) {
        return this.heap.pop();
    }
    const result = this.heap[0];
    this.swap(0, this.heap.length -1);
    this.heap.pop();
    let id = 0;
    const weight = this.heap[0][1];
    let cid;
    while ((this.leftChild(id) && this.leftChild(id)[1] < weight) || (this.rightChild(id) && this.rightChild(id)[1] < weight)) {
        cid = this.leftChildIndex(id);
        if (this.rightChild(id) && this.rightChild(id)[1] < this.leftChild(id)[1]) {
            cid = this.rightChildIndex(id);
        }
        this.swap(id, cid);
        id = cid;
    }
    return result;
}

PrioQ.prototype.leftChild = function(id) {
    const cid = this.leftChildIndex(id);
    return this.heap[cid];
}

PrioQ.prototype.rightChild = function(id) {
    const cid = this.rightChildIndex(id);
    return this.heap[cid];
}

PrioQ.prototype.leftChildIndex = function(id) {
    return 2*id + 1;
}

PrioQ.prototype.rightChildIndex = function(id) {
    return 2*id + 2;
}

Graph.prototype.dijkstra = function (start) {
    const queue = new PrioQ();
    const distance = {};
    const visited = {};
    let total = graph.edges[v1][v2];
    let preVertex = start;
    for(let vertex in graph.edges) {
        distance[vertex] = Number.POSITIVE_INFINITY;
        visited[vertex] = false;
    }
    visited[start] = true;
    distance[start] = 0;
    distance[v2] = graph.edges[v1][v2]
    for (let [vertex, weight] of Object.entries(graph.edges[start])) {
        queue.heappush(vertex, weight)
    }
    while (queue.heap.length !== 0) {
        const [minVertex, minWeight] = queue.heappop();
        if (!visited[minVertex]) {
            visited[minVertex] = true;
            
            for (let [vertex, weight] of Object.entries(graph.edges[minVertex])) {
                queue.heappush(vertex, weight + minWeight)
            }
            if (parseInt(minVertex) !== v2 && distance[minVertex] > minWeight) {
                console.log(`from ${preVertex} to ${minVertex}`)
                total += graph.edges[preVertex][minVertex]
                distance[minVertex] = minWeight;
            }
            preVertex = minVertex;
        }
    }

    if (Object.values(distance).includes(Number.POSITIVE_INFINITY)) return -1;
    return total
}
console.log(graph.dijkstra(v1))