/* 
Kruscal알고리즘은 주어진 N개의 정점을 갖는 그래프를 최단 간선으로 연결하여 
N-1개의 간선으로 연결된 트리를 만드는 알고리즘이다.

때문에 그리디로 최단 간선들을 선택하고, 중간 중간 그래프가 만들어지는 것을 
방지하면서 간선을 선택한다.

➡️ 그래프가 생기는 것을 방지하기 위해서는 Union-Find 알고리즘을 사용한다.
그래프를 만드는 것이 아닌 간선들을 선택하는 것 이기 때문에 union-find 확인을 위한 배열 하나만 필요하다.
*/

const input = [
    /*
    1 2 3
    1 3 2
    3 2 1
    2 5 2
    3 4 4
    7 3 6
    5 1 5
    1 6 2
    6 4 1
    6 5 3
    4 5 3
    6 7 4
    */
]

input.sort((a,b) => a[2] - b[2]) // weight를 기준으로 오름차순으로 정렬
let total = 0;
for (let i=0; i<input.length; i++) {
    const [v1,v2,w] = input[i];
    if (find(v1) !== find(v2)) { // circuit이 생기는것을 방지
        union(v1,v2);
        total += w; // 선택된 최소의 가중치의 합
        // 만약 n+1개의 집합으로 나누길 원한다면 마지막에 n개의 weight를 빼주면 된다.
        // big_weight = w;
    }
}

// 결국 Kruscal알고리즘은 union & find 알고리즘이라고 확인할 수 있겠다.

const parents = new Array(n+1).fill().map((v,i) => i) // i로 채워진 n+1 길이의 배열

function find(v) {
    if (parents[v] === v) {
        return v;
    }
    // 방법 1. 바로 root를 return한다 -> O(n)의 시간복잡도
    return parents[v];
    // 방법 2. 중간 중간 parents[v] 값을 업데이트 시켜준다.
    const root = find(parents[v]);
    parents[v] = root
    return root
}

function union(v1, v2) {
    const parent1 = find(v1);
    const parent2 = find(v2);
    if (parent1 !== parent2) {
        // 자기 자신을 return하던 parent2의 root를 parent1으로 바꿔줌으로써 union
        parents[parent2] = parent1;
    }
}