const input = [
    [
        7,
        [
            [1, 2],
            [2, 3],
            [1, 5],
            [5, 2],
            [5, 6],
            [4, 7],
        ],
    ],
    [
        10,
        [
            [8, 6],
            [5, 7],
            [9, 10],
            [7, 4],
            [1, 8],
            [5, 10],
            [7, 2],
        ],
    ],
    [
        10,
        [
            [6, 9],
            [9, 4],
            [4, 8],
            [9, 7],
            [6, 8],
            [10, 1],
            [10, 9],
        ],
    ],
];

function Graph() {
    this.edge = {};
    this.visited = {};
}

Graph.prototype.addVertex = function (vertex) {
    this.edge[vertex] = [];
    this.visited[vertex] = false;
};

Graph.prototype.addEdge = function (v1, v2) {
    if (!this.edge[v1]) {
        this.addVertex(v1);
    }
    if (!this.edge[v2]) {
        this.addVertex(v2);
    }
    this.edge[v1].push(v2);
    this.edge[v2].push(v1);
};

Graph.prototype.dfs = function (vertex) {
    if (this.visited[vertex]) {
        return;
    }
    this.visited[vertex] = true;
    const children = this.edge[vertex];
    for (let i = 0; i < children.length; i++) {
        this.dfs(children[i]);
    }
};

function answer(arr) {
    let result = 0;
    const graph = new Graph();
    for (let [v1,v2] of arr) {
        graph.addEdge(v1,v2);
    }
    graph.dfs(1);
    for (let vertex in graph.visited) {
        result += graph.visited[vertex] ? 1 : 0;
    }

    return result
}

for (let [num, arr] of input) {
    console.log(answer(arr));
}
