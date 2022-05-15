// 우선 순위 큐 템플릿 -> 각 아이템은 [vertex, weight]로 담겨있음
// 때문에 우선 순위는 item[1], weight값이 우선순위 입니다.
// 우선 순위 큐는 heap으로 구현되어있고, heap은 완전 이진트리이기때문에 배열로 간단하게 구현할 수 있음. 그래서 배열을 쓴 거야.
// 우선 순위 큐, Dijstra 문제가 나오면 이 템플릿을 사용하길...

function Graph() {
    this.edges = {};
}

Graph.prototype.addVertex = function (v) {
    this.edges[v] = {};
};

// 중복된 간선이 존재할 경우 더 낮은 가중치로 update
Graph.prototype.addEdge = function (v1, v2, w) {
    if (this.edges[v1][v2]) {
        this.edges[v1][v2] = this.edges[v1][v2] > w ? w : this.edges[v1][v2];
        return;
    }
    this.edges[v1][v2] = w;
};

function PrioQ() {
    this.heap = [];
}

PrioQ.prototype.getParentIndex = function(idx) {
    return Math.floor((idx - 1) / 2)
}

PrioQ.prototype.swap = function(id, pid) {
    temp = this.heap[id];
    this.heap[id] = this.heap[pid];
    this.heap[pid] = temp;
}

PrioQ.prototype.heappush = function (vertex, weight) {
    let id = this.heap.length;
    this.heap.push([vertex, weight])
    console.log(vertex, weight, id)
    let pid = this.getParentIndex(id);
    while (this.heap[pid]  && this.heap[pid][1] > weight) {
        this.swap(id, pid);
        id = pid;
        pid = this.getParentIndex(id);
    }
}

PrioQ.prototype.heappop = function () {
    if (this.heap.length === 1) {
        return this.heap.pop()
    }
    this.swap(0, this.heap.length - 1);
    const result = this.heap.pop();
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

const q = new PrioQ()
q.heappush("a",90)
q.heappush("b",15)
q.heappush("c",10)
q.heappush("d",7)
q.heappush("e",12)
q.heappush("f",2)
q.heappush("g",8)
q.heappush("h",3)

console.log(q.heap)
console.log(q.heappop(), q.heappop(), q.heappop(), q.heappop(), q.heappop(), q.heappop(), q.heappop(), q.heappop())
/*
[
  [ 'f', 2 ],
  [ 'h', 3 ],
  [ 'd', 7 ],
  [ 'c', 10 ],
  [ 'e', 12 ],
  [ 'b', 15 ],
  [ 'g', 8 ],
  [ 'a', 90 ]
]

[ 'f', 2 ] [ 'h', 3 ] [ 'd', 7 ] [ 'g', 8 ] [ 'c', 10 ] [ 'e', 12 ] [ 'b', 15 ] [ 'a', 90 ]
*/