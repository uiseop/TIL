let a = 1
let add = (b) => b = b+1

add(a);
console.log(a)

var obj = {v:1}
var obj_a = (b) => b.v = b.v+1

obj_a(obj)
console.log(obj)

function MAX(x,y){
    let ans
    ans = x >= y ? x : y
    return ans
}

console.log(MAX(0,3));
console.log(MAX(-1,5));
console.log(MAX(100,7));