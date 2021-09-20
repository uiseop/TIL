let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim();

const re = /\-/g;
const first_check = /^\-/;
let tot = 0;

// 양수와 음수로 시작하는 부분을 나눴음
// 하지만 문제에서는 양수들로만 식을 만들었기때문에 2가지 경우로 나누지 않아도 돼
// 좀 더 짧은식으로 풀이가 가능했던 부분임

if(first_check.test(input)){
    const spls = input.split(re)
    for(let spl of spls){
        let nums = spl.split(/\+/)
        let sum = 0;
        for(let num of nums){
            sum += Number(num)
        }
        tot -= sum
    }
}
else{
    const spls = input.split(re)
    for(let i in spls){
        let sum = 0
        if(i === '0'){
            let nums = spls[i].split(/\+/)
            for(let num of nums){
                sum += Number(num)
            }
            tot += sum
        }
        else{
            let nums = spls[i].split(/\+/)
            for(let num of nums){
                sum += Number(num)
            }
            tot -= sum
        }
    }
}

console.log(tot);