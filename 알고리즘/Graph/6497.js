let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n");

let idx = 1;
let flag = false;
while (!flag) {
    const [n,m] = input[idx-1].split(" ").map((num) => parseInt(num));
    const roads = [];
    
    for (let i=idx; i<input.length - 1; i++) {
        const data = input[i].split(" ").map((num) => parseInt(num))
        if (i === input.length - 2) {
            flag = true;
        }
        else if (data.length === 2) {
            idx = i + 1;
            break;
        }
        roads.push(input[i].split(" ").map((num) => parseInt(num)))
    }
    
    roads.sort((a,b) => a[2] - b[2])
    
    const parents = new Array(n).fill().map((v,i) => i)
    
    let costs = 0;
    
    for (let [x,y,z] of roads) {
        if (find(x) !== find(y)) {
            union(x,y)
            costs += z;
        }
    }
    
    function find(x) {
        if (parents[x] === x) {
            return x;
        }
        let parent = find(parents[x]);
        parents[x] = parent;
        return parent;
    }
    
    function union(x,y) {
        let X = find(x);
        let Y = find(y);
        if (X !== Y) {
            parents[Y] = X;
        }
    }

    // console.log(costs)
    // console.log(`this is parents ${parents}`)
    
    console.log(roads.reduce((total,n) => {
        return total + n[2]
    },0) - costs)

}