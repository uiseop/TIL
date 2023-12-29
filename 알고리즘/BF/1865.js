let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const N = +input[0];
const blockInfoList = input.slice(1).map((line) => line.split(" ").map(Number));

let score = 0;

const blocks = new Array(10).fill(null).map((_, idx) => {
  if (idx <= 3) {
    return new Array(10).fill(0);
  }
  return new Array(4).fill(0);
});

function isOne(element) {
  return element === 1;
}

function moveRight(option, r, c) {
  const lastIndex = blocks[r].findIndex(isOne);

  switch (option) {
    case 1:
      if (lastIndex === -1) {
        blocks[r][9] = 1;
      } else {
        blocks[r][lastIndex - 1] = 1;
      }
      return;
    case 2:
      if (lastIndex === -1) {
        blocks[r][9] = 1;
        blocks[r][8] = 1;
      } else {
        blocks[r][lastIndex - 1] = 1;
        blocks[r][lastIndex - 2] = 1;
      }
      return;
    case 3:
      const nextLastIndex = blocks[r + 1].findIndex(isOne);
      if (lastIndex === -1 && nextLastIndex === -1) {
        blocks[r][9] = 1;
        blocks[r + 1][9] = 1;
      } else if (lastIndex === -1) {
        blocks[r][nextLastIndex - 1] = 1;
        blocks[r + 1][nextLastIndex - 1] = 1;
      } else if (nextLastIndex === -1) {
        blocks[r][lastIndex - 1] = 1;
        blocks[r + 1][lastIndex - 1] = 1;
      } else {
        const minIndex = Math.min(lastIndex, nextLastIndex);
        blocks[r][minIndex - 1] = 1;
        blocks[r + 1][minIndex - 1] = 1;
      }
      return;
    default:
      break;
  }
}

function getColums(col) {
  const cols = [];
  const maxRow = col < 4 ? 10 : 4;
  for (let row = 0; row < maxRow; row++) {
    cols.push(blocks[row][col]);
  }
  return cols;
}

function moveDown(option, r, c) {
  const lastIndex = getColums(c).findIndex(isOne);

  switch (option) {
    case 1:
      if (lastIndex === -1) {
        blocks[9][c] = 1;
      } else {
        blocks[lastIndex - 1][c] = 1;
      }
      return;
    case 3:
      if (lastIndex === -1) {
        blocks[9][c] = 1;
        blocks[8][c] = 1;
      } else {
        blocks[lastIndex - 1][c] = 1;
        blocks[lastIndex - 2][c] = 1;
      }
      return;
    case 2:
      const nextLastIndex = getColums(c + 1).findIndex(isOne);
      if (lastIndex === -1 && nextLastIndex === -1) {
        blocks[9][c] = 1;
        blocks[8][c] = 1;
      } else if (lastIndex === -1) {
        blocks[nextLastIndex - 1][c] = 1;
        blocks[nextLastIndex - 1][c + 1] = 1;
      } else if (nextLastIndex === -1) {
        blocks[lastIndex - 1][c] = 1;
        blocks[lastIndex - 1][c + 1] = 1;
      } else {
        const minIndex = Math.min(lastIndex, nextLastIndex);
        blocks[minIndex - 1][c] = 1;
        blocks[minIndex - 1][c + 1] = 1;
      }
      return;
    default:
      break;
  }
}

function checkBlue() {
  let isChanged = false;

  for (let col = 6; col < 10; col++) {
    const cols = getColums(col);
    const sum = cols.reduce((acc, cur) => acc + cur);
    if (sum === 4) {
      score += 1;
      isChanged = true;
      for (let row = 0; row < 4; row++) {
        blocks[row].splice(col, 1);
        blocks[row].splice(4, 0, 0);
      }
    }
  }

  if (!isChanged) return;

  for (let col = 8; col >= 6; col--) {
    for (let row = 0; row < 4; row++) {
      let cur = col;
      while (blocks[row][cur] && !blocks[row][cur + 1]) {
        blocks[row][cur] = 0;
        blocks[row][cur + 1] = 1;
        cur += 1;
        if (cur === 9) break;
      }
    }
  }

  checkBlue();
}

function checkShallowBlue() {
  const cols4 = getColums(4);
  const cols5 = getColums(5);

  const sum4 = cols4.reduce((acc, cur) => acc + cur);
  const sum5 = cols5.reduce((acc, cur) => acc + cur);

  if (sum4 && sum5) {
    for (let row = 0; row < 4; row++) {
      blocks[row].splice(8, 2);
      blocks[row].splice(4, 0, 0, 0);
    }
  } else if (sum4 || sum5) {
    for (let row = 0; row < 4; row++) {
      blocks[row].splice(9, 1);
      blocks[row].splice(4, 0, 0);
    }
  }
}

function checkGreen() {
  let isChanged = false;
  for (let row = 6; row < 10; row++) {
    const rows = blocks[row];
    const sum = rows.reduce((acc, cur) => acc + cur);
    if (sum === 4) {
      score += 1;
      isChanged = true;
      blocks.splice(row, 1);
      blocks.splice(4, 0, [0, 0, 0, 0]);
    }
  }

  if (!isChanged) return;

  for (let row = 8; row >= 6; row--) {
    for (let col = 0; col < 4; col++) {
      let cur = row;
      while (blocks[cur][col] && !blocks[cur + 1][col]) {
        blocks[cur][col] = 0;
        blocks[cur + 1][col] = 1;
        cur += 1;
        if (cur === 9) break;
      }
    }
  }

  checkGreen();
}

function checkShallowGreen() {
  const row4 = blocks[4];
  const row5 = blocks[5];

  const sum4 = row4.reduce((acc, cur) => acc + cur);
  const sum5 = row5.reduce((acc, cur) => acc + cur);

  if (sum4 && sum5) {
    blocks.splice(8, 2);
    blocks.splice(4, 0, [0, 0, 0, 0], [0, 0, 0, 0]);
  } else if (sum4 || sum5) {
    blocks.splice(9, 1);
    blocks.splice(4, 0, [0, 0, 0, 0]);
  }
}

function laydownBlock(blockInfo) {
  const [t, r, c] = blockInfo;

  moveRight(t, r, c);
  moveDown(t, r, c);

  checkBlue();
  checkGreen();

  checkShallowBlue();
  checkShallowGreen();

  checkBlue();
  checkGreen();
}

for (const blockInfo of blockInfoList) {
  laydownBlock(blockInfo);
}

let count = 0;

function countBlue() {
  for (let r = 0; r < 4; r++) {
    for (let c = 6; c < 10; c++) {
      if (blocks[r][c]) count += 1;
    }
  }
}

function countGreen() {
  for (let r = 6; r < 10; r++) {
    for (let c = 0; c < 4; c++) {
      if (blocks[r][c]) count += 1;
    }
  }
}

countBlue();
countGreen();

console.log(score);
console.log(count);
