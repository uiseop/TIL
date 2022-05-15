let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n")
// let input = fs.readFileSync("test.txt").toString().split("\n");

const n = parseInt(input[0]);
const m = parseInt(input[1]);
const roads = [];

for (let i = 2; i < input.length; i++) {
    roads.push(input[i].split(" ").map((num) => parseInt(num)));
}

function Graph() {
    this.edge = {};
}

Graph.prototype.addVertex = function (v) {
    this.edge[v] = {};
};

Graph.prototype.addEdge = function (v1, v2, w) {
    if (this.edge[v1][v2]) {
        this.edge[v1][v2] = this.edge[v1][v2] > w ? w : this.edge[v1][v2]
    } else {
        this.edge[v1][v2] = w;
    }
};

const graph = new Graph();

for (let i = 1; i <= n; i++) {
    graph.addVertex(i);
}

roads.forEach(([v1, v2, w]) => {
    graph.addEdge(v1, v2, w);
})

Graph.prototype._extractMin = function (queue, distance) {
    let minDistance = Number.POSITIVE_INFINITY;
    let minVertex = null;
    for (let vertex in queue) {
        if (distance[vertex] < minDistance) {
            minDistance = distance[vertex];
            minVertex = vertex;
        }
    }
    return minVertex;
};

Graph.prototype.dijkstra = function (start) {
    // const visited = new Array(n + 1).fill(false);
    const queue = {};
    const distance = {};
    // 모든 정점에 대한 경로의 값을 무한대로 설정
    for (let vertex in this.edge) {
        distance[vertex] = Number.POSITIVE_INFINITY;
        // queue 객체에는 정점과 연결된 다른 정점들을 받아옴 -> 비교하려고
        queue[vertex] = this.edge[vertex];
    }

    distance[start] = 0;
    while (Object.keys(queue).length !== 0) {
        let minVertex = this._extractMin(queue, distance);
        // queue 객체에 있는 최단 거리의 정점을 지운다.
        delete queue[minVertex];

        for (let vertex in this.edge[minVertex]) {
            let temp = distance[minVertex] + this.edge[minVertex][vertex];
            if (temp < distance[vertex]) {
                distance[vertex] = temp;
            }
        }
    }
    for (let vertex in this.edge) {
        if (distance[vertex] === Number.POSITIVE_INFINITY) {
            distance[vertex] = 0;
        }
    }

    return distance;
};

const answer = []

for (let i = 1; i < n + 1; i++) {
    const result = Object.values(graph.dijkstra(i.toString()))
    answer.push(result);
}

answer.forEach((arr) => console.log(arr.join(" ")))
