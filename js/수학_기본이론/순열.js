// 3개의 알파벳을 모두 사용하여 만들 수 있는 단어의 수

let input = ["a", "b", "c"];
let count = 0;

// const permutation = (arr, s, t) => {
//     if (s == t) {
//         count += 1;
//         console.log(arr.join(" "));
//         return
//     }
//     for (let i=s; i < arr.length; i++) {
//         [arr[i], arr[s]] = [arr[s], arr[i]];
//         permutation(arr, s+1, t);
//         [arr[i], arr[s]] = [arr[s], arr[i]];
//     }
// }

// permutation(input, 0, 2);
// console.log(count);

const getPermutation = (arr, len) => {
    const result = []
    if (len === 1) return arr.map((el) => [el])
    
    arr.forEach((fixed, idx, origin) => {
        const rest = origin.slice(0,idx).concat(origin.slice(idx+1))
        const permutes = getPermutation(rest, len-1)
        permutes.forEach((permute) => result.push([fixed, ...permute]))
    })
    return result
}

console.log(getPermutation(input, 3))

/* output
a b c
a c b
b a c
b c a
c b a
c a b
6
*/