let fs = require("fs");
let [len,input] = fs.readFileSync("dev/stdin").toString().split('\n');


let answer = 0

let left = 0
let map = new Map()

let set = new Set(input)
if(set.size <= len) console.log(input.length)
else{
    // 초기값 세팅
    map.set(input[left],[left])
    let right = 1
    while(input[right] === input[left]) right += 1
    map.set(input[right],[right])
    right += 1

    // 탐색 시작
    while(right < input.length){
        if(map.has(input[right])){
            map.get(input[right]).push(right)
        }
        else{
            if(map.size == len){
                answer = answer < right - left ? right - left : answer

                let temp = left
                left = map.get(input[left]).pop() + 1
                map.delete(input[temp])
                map.set(input[right],[right])
            }
            else{
                map.set(input[right],[right])
            }
        }
        right += 1
    }
    console.log(answer);

}
