let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const K = +input[0];
const N = 2 ** K;
const [x, y] = input[1].split(" ").map(Number);

const ORIGN = [
  [0, 0],
  [0, 1],
  [1, 1],
];

const ORIGN_REVERSED = [
  [0, 0],
  [0, 1],
  [1, 0],
];

const REVERSED = [
  [0, 0],
  [1, 0],
  [1, 1],
];

const REVERSED_REVERSED = [
  [0, 0],
  [1, 0],
  [1, -1],
];

const isHole = -1;

const floor = Array(N)
  .fill(null)
  .map((_) => Array(N).fill(0));

floor[y - 1][x - 1] = isHole;

function isOutofRange(r, c) {
  if (r >= 0 && r < N && c >= 0 && c < N) return false;
  return true;
}

function backtracking(r, c, floor, count) {
  /** return 의 조건
   * 1. r === K - 1 || c === K - 1
   * 2. c 가 현재 범위를 넘을 때
   * 3. r 이 현재 범위를 넘을 때 <- 얘는 1번 조건에서 닿아 리턴되기 때문에 그냥 pass
   * 4. 현재 공간은 체크할 필요 없어 넘어갈 때
   * 4-1. 이는 2가 될 수 있고
   * 4-2. 아니면 그냥 오른쪽으로 넘어갈 수 있음
   */

  if (r === N - 1 && c === N - 1) {
    floor.reverse();

    console.log(floor.map((item) => item.join(" ")).join("\n"));
    return true;
  }

  if (floor[r][c] || floor[r][c] === isHole) {
    if (c + 1 === N) {
      return backtracking(r + 1, 0, floor, count);
    } else {
      return backtracking(r, c + 1, floor, count);
    }
  }

  if (isOutofRange(r, c)) {
    if (c === N) return backtracking(r + 1, 0, floor, count);

    return backtracking(r, c + 1, floor, count);
  }

  let result;
  let isOriginPossible = true;
  let isOriginReversePossible = true;
  let isReversePossible = true;
  let isReverseReversePossible = true;

  for (const [dr, dc] of ORIGN) {
    const nr = r + dr;
    const nc = c + dc;

    if (!isOutofRange(nr, nc) && !floor[nr][nc]) continue;
    isOriginPossible = false;
  }

  if (isOriginPossible) {
    for (const [dr, dc] of ORIGN) {
      const nr = r + dr;
      const nc = c + dc;

      floor[nr][nc] = count;
    }

    result = backtracking(r, c + 1, floor, count + 1);
    if (result) return result;

    for (const [dr, dc] of ORIGN) {
      const nr = r + dr;
      const nc = c + dc;

      floor[nr][nc] = 0;
    }
  }

  for (const [dr, dc] of REVERSED) {
    const nr = r + dr;
    const nc = c + dc;

    if (!isOutofRange(nr, nc) && !floor[nr][nc]) continue;
    isReversePossible = false;
  }

  if (isReversePossible) {
    for (const [dr, dc] of REVERSED) {
      const nr = r + dr;
      const nc = c + dc;

      floor[nr][nc] = count;
    }

    result = backtracking(r, c + 1, floor, count + 1);
    if (result) return result;

    for (const [dr, dc] of REVERSED) {
      const nr = r + dr;
      const nc = c + dc;

      floor[nr][nc] = 0;
    }
  }

  for (const [dr, dc] of ORIGN_REVERSED) {
    const nr = r + dr;
    const nc = c + dc;

    if (!isOutofRange(nr, nc) && !floor[nr][nc]) continue;
    isOriginReversePossible = false;
  }

  if (isOriginReversePossible) {
    for (const [dr, dc] of ORIGN_REVERSED) {
      const nr = r + dr;
      const nc = c + dc;

      floor[nr][nc] = count;
    }

    result = backtracking(r, c + 1, floor, count + 1);
    if (result) return result;

    for (const [dr, dc] of ORIGN_REVERSED) {
      const nr = r + dr;
      const nc = c + dc;

      floor[nr][nc] = 0;
    }
  }

  for (const [dr, dc] of REVERSED_REVERSED) {
    const nr = r + dr;
    const nc = c + dc;

    if (!isOutofRange(nr, nc) && !floor[nr][nc]) continue;
    isReverseReversePossible = false;
  }

  if (isReverseReversePossible) {
    for (const [dr, dc] of REVERSED_REVERSED) {
      const nr = r + dr;
      const nc = c + dc;

      floor[nr][nc] = count;
    }

    result = backtracking(r, c + 1, floor, count + 1);
    if (result) return result;

    for (const [dr, dc] of REVERSED_REVERSED) {
      const nr = r + dr;
      const nc = c + dc;

      floor[nr][nc] = 0;
    }
  }

  return result;
}

const result = backtracking(0, 0, floor, 1);

if (!result) console.log(-1);
