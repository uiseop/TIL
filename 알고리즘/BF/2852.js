let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs
//   .readFileSync("test.txt")
//   .toString()
//   .trim()
//   .split("\n")
//   .map((str) => str.replace("\r", ""));

const END_TIME = 48 * 60;

let i = 0;

const N = Number(input[i++]);

const points = [0, 0, 0];
const times = [0, 0, 0];
let past = 0;

for (let j = 0; j < N; j++) {
  let [team, time] = input[i++].split(" ");
  team = Number(team);

  const other = team === 1 ? 2 : 1;

  const [hour, min] = time.split(":").map((t) => Number(t));

  const T = hour * 60 + min;

  if (points[other] < points[team]) {
    times[team] += T - past;
  } else if (points[other] > points[team]) {
    times[other] += T - past;
  }
  
  points[team] += 1;
  past = T;
}

if (points[1] < points[2]) {
  times[2] += END_TIME - past;
} else if (points[1] > points[2]) {
  times[1] += END_TIME - past;
}

for (let i = 1; i < 3; i++) {
  const hour = String(Math.floor(times[i] / 60)).padStart(2,'0');
  const min = String(times[i] % 60).padStart(2,'0');
  console.log(`${hour}:${min}`);
}
