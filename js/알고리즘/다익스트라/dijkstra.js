function Graph() {
    this.edges = {};
}

Graph.prototype.addVertex = function (v) {
    this.edges[v] = {};
};

Graph.prototype.addEdge = function (v1, v2, weight) {
    this.edges[v1][v2] = weight;
};

Graph.prototype._extractMin = function (queue, dist) {
    let minDistance = Number.POSITIVE_INFINITY;
    let minVertex = null;

    for (let vertex in queue) {
        if (dist[vertex] < minDistance) {
            minDistance = dist[vertex];
            minVertex = vertex;
        }
    }
    return minVertex;
};

Graph.prototype.dijkstra = function (start) {
    const dist = {};
    const queue = {};
    for (let vertex in this.edges) {
        dist[vertex] = Number.POSITIVE_INFINITY;
        queue[vertex] = this.edges[vertex];
    }

    dist[start] = 0;
    while (Object.keys(queue).length != 0) {
        let minVertex = this._extractMin(queue, dist);
        delete queue[minVertex];

        for (let neighbor in this.edges[minVertex]) {
            let temp = dist[minVertex] + this.edges[minVertex][neighbor];
            if (temp < dist[neighbor]) dist[neighbor] = temp;
        }
    }

    for (let vertex in this.edges) {
        if (dist[vertex] === Number.POSITIVE_INFINITY) {
            delete dist[vertex];
        }
    }

    return dist;
};


let graph = new Graph();
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")

graph.addEdge("A", "B", 10)
graph.addEdge("A", "C", 3)
graph.addEdge("B", "C", 1)
graph.addEdge("B", "D", 2)
graph.addEdge("C", "B", 4)
graph.addEdge("C", "D", 8)
graph.addEdge("C", "E", 2)
graph.addEdge("D", "E", 7)
graph.addEdge("E", "D", 9)

console.log(graph)
console.log(graph.dijkstra("A"))