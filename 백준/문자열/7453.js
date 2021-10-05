let fs = require("fs");
let [n, ...arrays] = fs.readFileSync("dev/stdin").toString().trim().split(/\r\n/);

let a = [], b = [], c = [], d = []
for(let nums of arrays){
    nums = nums.split(' ')
    a.push(Number(nums[0]))
    b.push(Number(nums[1]))
    c.push(Number(nums[2]))
    d.push(Number(nums[3]))
}

let sum = new Map()
let answer = 0

for(let A of a){
    for(let B of b){
        let tot = A + B
        if(sum.has(-1*tot)) sum.set(-1*tot, sum.get(-1*tot) + 1)
        else sum.set(tot*-1,1)
    }
}

for(let C of c){
    for(let D of d){
        let tot = C + D
        if(sum.has(tot)) answer += sum.get(tot)
    }
}

console.log(answer);