let fs = require("fs");
const { toNamespacedPath } = require("path");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n");

const T = parseInt(input[0]);

function Queue() {
    this.items = [];
    this.head = 0;
    this.tail = 0;
}

Queue.prototype.enque = function (vertex) {
    this.items.push(vertex);
    this.tail += 1;
}

Queue.prototype.deqeue = function () {
    const result = this.items[this.head];
    this.head += 1;
    return result;
}

Queue.prototype.isEmpty = function() {
    return this.head === this.tail;
}

function Graph() {
    this.items = {}
}

Graph.prototype.addVertex = function (v) {
    this.items[v] = [];
}

Graph.prototype.addEdge = function (arr) {
    const [from, to] = arr;
    this.items[to].push(from)
}

Graph.prototype.find = function (start, visited, time) {
    let total = time[start];
    visited[start] = true;
    const q = new Queue();
    const next_q = new Queue();
    q.enque(start);
    while (true) {
        let temp = 0;
        while (!q.isEmpty()) {
            const current = q.deqeue();
            for (let next_vertex of this.items[current]) {
                if (!visited[next_vertex]) {
                    visited[next_vertex] = true;
                    temp = temp < time[next_vertex] ? time[next_vertex] : temp;
                    next_q.enque(next_vertex);
                }
            }
        }
        total += temp;
        temp = 0;
        while (!next_q.isEmpty()) {
            const current = next_q.deqeue();
            for (let next_vertex of this.items[current]) {
                if (!visited[next_vertex]) {
                    visited[next_vertex] = true;
                    temp = temp < time[next_vertex] ? time[next_vertex] : temp;
                    q.enque(next_vertex);
                }
            }
        }
        total += temp;
        if (q.isEmpty()) break;
    }
    return total
}

let j=1;
for (let i=0; i<T; i++) {
    const [N,K] = input[j++].split(" ").map((num) => parseInt(num))
    const temp_time = [0]
    const time_arr = input[j++].split(" ").map((num) => parseInt(num))
    const time = temp_time.concat(time_arr)
    const graph = new Graph();

    for (let n=1; n<=N; n++) {
        graph.addVertex(n);
    }
    for (let k=0; k<K; k++) { // from, to 를 바꿔서 저장
        graph.addEdge(input[j++].split(" ").map((num) => parseInt(num)))
    }
    const start = parseInt(input[j++]);
    const visited = new Array(N+1).fill(false);
    console.log(graph.find(start,visited, time));
}