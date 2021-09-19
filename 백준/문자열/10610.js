let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim().split("");

// 오름차순으로 정렬 -> sort함수 사용. 매개변수로 사용되는 Array의 요소들 비교

input = input.sort((a,b) => b-a)
if(!input.includes('0')) console.log(-1)
else{
    let sum = 0;
    for(let i of input){
        sum += Number(i)
    }
    if(sum%3 != 0){
        console.log(-1)
    }
    else{
        console.log(input.join(''));
    }
}
