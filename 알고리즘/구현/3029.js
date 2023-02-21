let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs.readFileSync("test.txt").toString().trim().split("\n").map((str) => str.replace('\r', ''));

let [cur_time, throw_time] = input.map((t) => t.split(':').reduce((acc,cur,idx,arr) => acc + 60**(arr.length - (idx+1)) * Number(cur), 0))

if (throw_time <= cur_time) {
    throw_time += 24 * 60 * 60
}

let t_answer = throw_time - cur_time

const t_hour = Math.floor(t_answer / 3600)
t_answer -= t_hour * 3600
const t_min = Math.floor(t_answer / 60)
t_answer -= t_min * 60

const paddingZero = (num) => num.toString().padStart(2, '0')

console.log(`${paddingZero(t_hour)}:${paddingZero(t_min)}:${paddingZero(t_answer)}`)