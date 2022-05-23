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
    this.len = {}
}

Graph.prototype.addVertex = function (v) {
    this.items[v] = {};
    this.len[v] = 0;
}

Graph.prototype.addEdge = function (from, to) {
    this.items[from][to] = true;
    this.len[from] += 1;
}

let j=1;
for (let i=0; i<T; i++) {
    const [N,K] = input[j++].split(" ").map((num) => parseInt(num))
    const temp_time = [0]
    const time_arr = input[j++].split(" ").map((num) => parseInt(num))
    const time = temp_time.concat(time_arr)
    const from_graph = new Graph();
    const to_graph = new Graph();
    const q = new Queue();

    for (let n=1; n<=N; n++) {
        to_graph.addVertex(n);
        from_graph.addVertex(n);
    }
    for (let k=0; k<K; k++) { // from, to 를 바꿔서 저장
        const [from,to] = input[j++].split(" ").map((num) => parseInt(num))
        to_graph.addEdge(to, from)
        from_graph.addEdge(from, to)
    }

    for (let [key,value] of Object.entries(to_graph.items)) {
        if (Object.entries(value).length === 0) {
            q.enque(key);
        }
    }

    const target = parseInt(input[j++])
    const temp = new Array(N+1).fill(0);

    while (!q.isEmpty()) {
        const f_node = q.deqeue();
        if (f_node === target) break;
        for (let t_node of Object.keys(from_graph.items[f_node])) {
            if (temp[t_node] < time[f_node]) {
                temp[t_node] = time[f_node]
            }
            delete to_graph.items[t_node][f_node];
            to_graph.len[t_node] -= 1;
            if (to_graph.len[t_node] === 0){
            // if (Object.keys(to_graph.items[t_node]).length === 0) {
                q.enque(t_node)
                time[t_node] += temp[t_node];
            }
        }
    }
    console.log(time[target]);
}