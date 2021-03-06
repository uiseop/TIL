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
    // toFixed ๐ ์์์  n๋ฒ์งธ๊น์ง ๋ฐ์ฌ๋ฆผํด์ ๊ตฌํ๋ค. ๋ฐ์ฌ๋ฆผ์ฌ์ฉ
    // ๋ฐ์ฌ๋ฆผ ์ฌ์ฉ ๋ฌธ์ ๊ฐ ์์ ์ ์์ผ๋ ์์งํ๋๋ก
    hash.set(tree, ((hash.get(tree)/len)*100).toFixed(4))
}

// Map์๋ฃ๊ตฌ์กฐ์ ์ ๋ ฌํ๋ ๋ฐฉ๋ฒ์ ๋ฐฐ์ ๋ค.
// Map์๋ฃ๊ตฌ์กฐ๋ฅผ key,value ํํ์ ๋ฐฐ์ด๋ก ๋ง๋  ํ ๋ฐฐ์ด์์ ์ ๋ ฌํ๋ฏ์ด ์ฌ์ฉ
// sort์์ ๋ณ๋ค๋ ํจ์๊ฐ ์์ผ๋ฉด key๊ฐ์ ๊ธฐ์ค์ผ๋ก ์ ๋ ฌ์ ์ํ
// sort์์ index๋ฅผ ๋ฃ์ผ๋ฉด ํด๋น ์ธ๋ฑ์ค ๊ธฐ์ค์ผ๋ก ์ ๋ ฌ์ ์ํํจ
const mapSort = new Map([...hash.entries()].sort())
console.log(mapSort);