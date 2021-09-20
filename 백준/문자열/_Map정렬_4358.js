let fs = require("fs");
let input = fs.readFileSync("dev/stdin").toString().trim().split('\r\n');

let hash = new Map();
let len = input.length;
for(let tree of input){
    if(tree === '') continue
    if(hash.has(tree)){
        hash.set(tree, hash.get(tree) + 1)
    }
    else{
        hash.set(tree,1)
    }
}

for(let tree of hash.keys()){
    // toFixed 👉 소수점 n번째까지 반올림해서 구한다. 반올림사용
    // 반올림 사용 문제가 있을 수 있으니 숙지하도록
    hash.set(tree, ((hash.get(tree)/len)*100).toFixed(4))
}

// Map자료구조의 정렬하는 방법을 배웠다.
// Map자료구조를 key,value 형태의 배열로 만든 후 배열에서 정렬하듯이 사용
// sort안에 별다는 함수가 없으면 key값을 기준으로 정렬을 수행
// sort안에 index를 넣으면 해당 인덱스 기준으로 정렬을 수행함
const mapSort = new Map([...hash.entries()].sort())
console.log(mapSort);