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
}