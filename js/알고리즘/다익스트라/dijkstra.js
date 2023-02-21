// function Graph() {
//     this.edges = {};
// }

// Graph.prototype.addVertex = function (v) {
//     this.edges[v] = {};
// };

// Graph.prototype.addEdge = function (v1, v2, weight) {
//     this.edges[v1][v2] = weight;
// };

// Graph.prototype._extractMin = function (queue, dist) { // 이 부분은 heap을 통해 구현하면 시간복잡도를 확 줄일 수 있음
//     let minDistance = Number.POSITIVE_INFINITY;
//     let minVertex = null;

//     for (let vertex in queue) {
//         if (dist[vertex] < minDistance) {
//             minDistance = dist[vertex];
//             minVertex = vertex;
//         }
//     }
//     return minVertex;
// };

// Graph.prototype.dijkstra = function (start) {
//     const dist = {};
//     const queue = {};
//     for (let vertex in this.edges) {
//         dist[vertex] = Number.POSITIVE_INFINITY;
//         queue[vertex] = this.edges[vertex];
//     }

//     dist[start] = 0;
//     while (Object.keys(queue).length != 0) {
//         let minVertex = this._extractMin(queue, dist);
//         delete queue[minVertex];

//         for (let neighbor in this.edges[minVertex]) {
//             let temp = dist[minVertex] + this.edges[minVertex][neighbor];
//             if (temp < dist[neighbor]) dist[neighbor] = temp;
//         }
//     }

//     for (let vertex in this.edges) {
//         if (dist[vertex] === Number.POSITIVE_INFINITY) {
//             delete dist[vertex];
//         }
//     }

//     return dist;
// };

function Graph() {
    this.edges = new Map();
}

Graph.prototype.addVertex = function (node) {
    if (this.edges.get(node)) return;
    this.edges.set(node, new Map());
};

Graph.prototype.addEdge = function (v1, v2, w) {
    const edges = this.edges.get(v1);
    if (edges.get(v2)) {
        edges.set(v2, Math.min(edges.get(v2), w));
    } else {
        edges.set(v2, w);
    }
};

function Heap() {
    this.items = []
}

Heap.prototype.swap = function (idx1, idx2) {
    const temp = this.items[idx1]
    this.items[idx1] = this.items[idx2]
    this.items[idx2] = temp
}

Heap.prototype.heappush = function (node, weight) {
    if (!this.items) return this.items.push({node, weight})
    let idx = this.items.length
    this.items.push({node, weight})
    while (idx > 0) {
        const pid = Math.floor((idx-1) / 2)
        if (this.items[pid].weight > this.items[idx].weight) {
            this.swap(pid, idx)
            idx = pid
        }
    }
}

Heap.prototype.heappop = function () {
    let idx = this.arr.length - 1
    this.swap(0, idx)
    idx = 0
    const ret = this.arr.pop()
    if (this.arr.length > 1) {
        while (true) {
            const left = 2*idx + 1
            const right = 2*idx + 2
            if (this.arr[left] && this.arr[right]) {
                if (this.arr[left] <= this.arr[right] && this.arr[left] < this.arr[idx]) {
                    this.swap(idx, left)
                    idx = left
                } else if (this.arr[left] > this.arr[right] && this.arr[right] < this.arr[idx]) {
                    this.swap(idx, right)
                    idx = right
                } else break
            } else if (this.arr[left] && this.arr[left] < this.arr[idx]) {
                this.swap(idx, left)
                idx = left
            } else break
        }
    }
    return ret
}

Graph.prototype.dijkstra = function (start) {
    const dist = new Map()
    const queue = new Heap()
    for (let v of this.edges.keys) {
        dist.set(v, Number.POSITIVE_INFINITY)
        queue.set(v, this.edges[v])
    }
    dist.set(start, 0)
    
}

let graph = new Graph();
graph.addVertex("A");
graph.addVertex("B");
graph.addVertex("C");
graph.addVertex("D");
graph.addVertex("E");

graph.addEdge("A", "B", 10);
graph.addEdge("A", "C", 3);
graph.addEdge("B", "C", 1);
graph.addEdge("B", "D", 2);
graph.addEdge("C", "B", 4);
graph.addEdge("C", "D", 8);
graph.addEdge("C", "E", 2);
graph.addEdge("D", "E", 7);
graph.addEdge("E", "D", 9);

// console.log(graph);
// console.log(graph.dijkstra("A"))
