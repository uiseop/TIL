let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim();

// <>에 문자 하나 이상 포함하는 문자열. 괄호로 묶어서 해당 조건또한 포함함
// 괄호를 안하면 <>조건은 포함되지않고 나눠짐
let re = /(<.*?>|\s)/g
let tmp = input.split(re)
let result = []

tmp.map((word) => {
    // 정규표현식.test를 했을때 true면 <>인것이니까 그냥 추가
    if(re.test(word)){
        result += word
    }
    else{
        // 문자열 뒤집기 👉 Array형식으로 만든 뒤 reverse 👉 다시 문자열로
        let rev = word.split('').reverse().join('')
        result += rev
    }
})

console.log(result);