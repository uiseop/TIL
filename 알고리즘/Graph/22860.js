let fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";
let input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split("\n")
  .map((str) => str.replace("\r", ""));

const directoryMap = new Map();

class Directory {
  constructor() {
    this.directories = new Map();
    this.files = new Set();
  }

  addDirectory(dirName) {
    const directory = directoryMap.get(dirName);
    this.directories.set(dirName, directory);
  }

  addFile(fName) {
    this.files.add(fName);
  }

  getTotalFiles() {
    let count = this.files.size;
    const set = this.files;

    for (const dir of this.directories.values()) {
      const result = dir.getTotalFiles();

      count += result.count;
      result.set.forEach((file) => {
        set.add(file);
      });
    }

    this.count = count;

    return {
      count,
      set,
    };
  }
}

const [N, M] = input[0].split(" ").map(Number);

const main = new Directory();

directoryMap.set("main", main);

for (let i = 1; i <= N + M; i++) {
  const [P, F, C] = input[i].split(" ");

  if (!directoryMap.has(P)) directoryMap.set(P, new Directory());

  if (Number(C) === 1 && !directoryMap.has(F)) {
    directoryMap.set(F, new Directory());
  }
}

directoryMap.set("main", main);

for (let i = 1; i <= N + M; i++) {
  const [P, F, C] = input[i].split(" ");
  const directory = directoryMap.get(P);

  if (Number(C) === 1) {
    // F는 Directory
    directory.addDirectory(F);
  } else {
    // F 는 file
    directory.addFile(F);
  }
}

main.getTotalFiles();

for (let i = N + M + 2; i < input.length; i++) {
  const query = input[i].split("/");

  const dir = directoryMap.get(query.at(-1));

  console.log(dir.files.size, dir.count);
}
