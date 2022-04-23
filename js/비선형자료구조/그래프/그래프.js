// 방향 그래프 - 인접 리스트로 구현

function Graph() {
    this.edge = {};
}

Graph.prototype.addVertex = function (v) {
    // 정점 추가, 정점은 여러 정점들과 연결될 수 있음
    this.edge[v] = [];
};

Graph.prototype.addEdge = function (v1, v2) {
    // 두 정점을 연결하는 간선 추가
    this.edge[v1].push(v2);
};

let graph = new Graph();
let vertices = ["A", "B", "C", "D", "E"];

for (let i = 0; i < vertices.length; i++) {
    graph.addVertex(vertices[i]); // 정점 추가
}

graph.addEdge("A", "B");
graph.addEdge("A", "C");
graph.addEdge("A", "D");
graph.addEdge("C", "G");
graph.addEdge("D", "G");
graph.addEdge("D", "G");
graph.addEdge("D", "H");
graph.addEdge("B", "E");
graph.addEdge("B", "F");
graph.addEdge("E", "I");

console.log(graph.edge)

/*
{
  A: [ 'B', 'C', 'D' ],
  B: [ 'E', 'F' ],
  C: [ 'G' ],
  D: [ 'G', 'G', 'H' ],
  E: [ 'I' ]
}
*/

Graph.prototype.removeEdge = function(v1, v2) {
    if (this.edge[v1]) {
        let idx = this.edge[v1].indexOf(v2);
        if (idx !== -1) {
            this.edge.splice(idx,1)
        }

        if (this.edge[v1].length === 0) {
            delete this.edge[v1];
        }
    }
}

Graph.prototype.removeVertex = function(v) {
    if (this.edge[v] === undefined) return;
    let nodes = [...this.edge[v]]; // immurable한 속성을 사용해서 연결된 모든 정점들을 삭제한다.
    for(let node of nodes) {
        this.removeEdge(v, node)
    } // 방향 그래프이기때문에 양쪽 삭제할 필요 없음
}

Graph.prototype.sizeVertex = function () {
    return Object.keys(this.edge).length;
}

Graph.prototype.sizeEdge = function() {
    return Object.values(this.edge).length
}