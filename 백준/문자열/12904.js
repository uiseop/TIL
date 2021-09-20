let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim().split('\r\n');

let answer = 0;
const dfs = (str, toStr) => {
    if(str.length === toStr.length){
        if(str === toStr)   answer = 1
        return
    }
    else{
        dfs(str+'A',toStr)
        let rev = [...str].reverse().join('') + 'B'
        dfs(rev,toStr)
    }
}


const S = input[0]
const T = input[1]

dfs(S,T)
console.log(answer);
