let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [n,m] = input[0].split(" ").map((num) => parseInt(num))

const edges = [];
for(let i=1; i<input.length; i++) {
    edges.push(input[i].split(" ").map((num) => parseInt(num)))
}

function sortAscendWeight(a,b) {
    const [f1,t1,w1] = a;
    const [f2,t2,w2] = b;
    return w1-w2;
}

edges.sort((a,b) => sortAscendWeight(a,b));

const parents = new Array(n+1).fill().map((v,i) => i);

let setParent = Array.from(new Set(parents.map((node) => find(node)))).length
let total = 0;
let bigCost = 0;

for (let i=0; i<edges.length; i++) {
    const [v1,v2,w] = edges[i];
    if (find(v1) !== find(v2)) {
        total += w;
        v1 < v2 ? union(v1,v2) : union(v2,v1)
        bigCost = w;
    }
}

console.log(total - bigCost)

function union(x,y) {
    const pX = find(x)
    const pY = find(y)
    if (pX !== pY) {
        parents[pY] = pX;
    }
}

function find(x) {
    if (parents[x] === x) {
        return x;
    }
    // find의 최적화 -> path Compression
    // 그냥 root노드를 찾지 않고, 찾는 즉시 update를 수행해줌.
    const pX = find(parents[x])
    parents[x] = pX;
    return pX;
}