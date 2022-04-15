// const input = [1,2,7]
// const input = [2,3,10]
const input = [3,5,23]

const n = input[2]
const a = input[0]
const d = input[1]

if ((n - a) % d !== 0) {
    console.log(-1)
} else {
    console.log((n-a) / d + 1)
}