const input = [
    // TC: 1
    ["00110", "00010", "00110", "00000", "01011"],
    // TC: 2
    ["00110", "00010", "00110", "00010", "01011"],
    // TC: 3
    [
        "1111111100",
        "1111111101",
        "1111111101",
        "1000111101",
        "1010111101",
        "1010011101",
        "1011011101",
        "1011011101",
        "1011000001",
        "0011111111",
    ],
];

function Queue() {
    this.arr = [];
    this.tail = 0;
    this.head = 0;
}

Queue.prototype.deque = function () {
    if (this.isEmpty()) {
        return undefined;
    }
    const result = this.arr[this.head];
    delete this.arr[this.head];
    this.head += 1;
    return result;
};

Queue.prototype.isEmpty = function () {
    return this.head === this.tail;
};

Queue.prototype.enque = function (value) {
    this.arr.push(value);
    this.tail += 1;
};

const dr = [1, -1, 0, 0];
const dc = [0, 0, 1, -1];

function answer(test) {
    const q = new Queue();
    const width = test.length;
    const visited = Array.from(Array(width), () => Array(width).fill(false))
    // console.log(visited)
    q.enque([width - 1, 0, 0]);
    visited[width-1][0] = 1;
    while (!q.isEmpty()) {
        let [r, c, count] = q.deque();
        for (let i = 0; i < 4; i++) {
            let nr = r + dr[i];
            let nc = c + dc[i];
            if (0 <= nr && nr < width && 0 <= nc && nc < width && test[nr][nc] === "0" && !visited[nr][nc]) {
                visited[nr][nc] = count + 1;
                q.enque([nr,nc, count + 1]);
                if (nr === 0 && nc === width-1) {
                    break
                }
            }
        }
    }
    return visited[0][width-1] ? visited[0][width-1] + 1 : -1
}

for (let test of input) {
    console.log(answer(test));
}
