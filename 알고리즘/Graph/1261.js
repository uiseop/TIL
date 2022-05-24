let fs = require("fs");
const { toNamespacedPath } = require("path");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n");

const [m, n] = input[0].split(" ").map((num) => parseInt(num));
input.splice(0,1);
const maze = input.map((row) => row.split("").map(Number))

const dr = [1, -1, 0, 0];
const dc = [0, 0, 1, -1];

const visited = Array.from({ length: n }, () => new Array(m).fill(0));

const heap = new Heap();
visited[0][0] = true

function Heap() {
    this.items = [];
}

Heap.prototype.parentIndex = function (idx) {
    return Math.floor((idx - 1) / 2);
};

Heap.prototype.parent = function (idx) {
    return this.items[this.parentIndex(idx)];
};

Heap.prototype.swap = function (idx, pid) {
    const temp = this.items[pid];
    this.items[pid] = this.items[idx];
    this.items[idx] = temp;
};

Heap.prototype.heappush = function (r,c,aoj) {
    this.items.push([r,c,aoj]);
    let idx = this.items.length - 1;
    while (this.parent(idx) && this.parent(idx)[2] > aoj) {
        let pid = this.parentIndex(idx);
        this.swap(pid, idx);
        idx = pid;
    }
};

Heap.prototype.left = function (idx) {
    return this.items[this.leftIndex(idx)]
}

Heap.prototype.leftIndex = function (idx) {
    return 2*idx + 1
}

Heap.prototype.right = function (idx) {
    return this.items[this.rightIndex(idx)]
}

Heap.prototype.rightIndex = function (idx) {
    return 2*idx + 2
}

Heap.prototype.heappop = function () {
    if (this.items.length === 1) {
        return this.items.pop();
    }
    this.swap(0, this.items.length - 1);
    const result = this.items.pop();
    let idx = 0;
    const aoj = this.items[idx][2];
    while ((this.left(idx) && this.left(idx)[2] < aoj) || (this.right(idx) && this.right(idx)[2] < aoj)) {
        let cid = this.leftIndex(idx);
        if (this.right(idx) && this.right(idx)[2] < this.left(idx)[2]) {
            cid = this.rightIndex(idx);
        }
        this.swap(idx,cid);
        idx = cid;
    }
    return result;
}

function bfs(x,y) {
    heap.heappush(x,y,0);
    while (heap.items.length !== 0) {
        const [r,c,aoj] = heap.heappop();
        if (r === n-1 && c === m-1) return aoj;
        for (let i=0; i<4; i++) {
            const nr = r + dr[i];
            const nc = c + dc[i];
            if (0 <= nr && nr < n && 0 <= nc && nc < m && !visited[nr][nc]) {
                visited[nr][nc] = true;
                if (maze[nr][nc]) {
                    heap.heappush(nr,nc,aoj+1);
                } else {
                    heap.heappush(nr,nc,aoj)
                }
            }
        }
    }
}

console.log(bfs(0,0));



// function bfs(r, c, visited, aoj) {
//     if (heap.items.length !== 0 && heap.items[0] <= aoj) return;
//     if (r === n - 1 && c === m - 1) {
//         heap.heappush(aoj);
//         return;
//     }
//     const new_visited = visited.map(v => v.slice())
//     for (let i = 0; i < 4; i++) {
//         const nr = r + dr[i];
//         const nc = c + dc[i];
//         if (0 <= nr && nr < n && 0 <= nc && nc < m && !new_visited[nr][nc]) {
//             new_visited[nr][nc] = true;
//             if (maze[nr][nc] === 1) {
//                 bfs(nr, nc, new_visited, aoj + 1);
//             } else {
//                 bfs(nr, nc, new_visited, aoj);
//             }
//         }
//     }
// }

// 알고스팟

