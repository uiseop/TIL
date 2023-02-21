let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs
    .readFileSync("test.txt")
    .toString()
    .trim()
    .split("\n")
    .map((str) => str.replace("\r", ""));

const [N, m, ...bus] = input;

const n = Number(N);

const weights = new Map();

for (let b of bus) {
    let [v1, v2, w] = b.split(" ").map(Number);
    v1 -= 1;
    v2 -= 1;
    if (weights.has(v1)) {
        const w_v1 = weights.get(v1);
        if (w_v1.has(v2)) {
            w_v1.set(v2, Math.min(w_v1.get(v2), w));
        } else {
            w_v1.set(v2, w);
        }
    } else {
        weights.set(v1, new Map());
        weights.get(v1).set(v2, w);
    }
}

const dist = new Array(Number(n))
    .fill(null)
    .map((i) => new Array(Number(n)).fill(Number.POSITIVE_INFINITY));

for (let key of weights.keys()) {
    for (let val of weights.get(key).keys()) {
        dist[key][val] = weights.get(key).get(val);
    }
}

for (let i = 0; i < n; i++) {
    dist[i][i] = 0;
}

for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
        }
    }
}

for (let i = 0; i < Number(n); i++) {
    console.log(dist[i].map((num) => {
        if (num === Number.POSITIVE_INFINITY) return 0
        return num
    }).join(' '));
}
