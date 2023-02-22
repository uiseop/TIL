let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs
//     .readFileSync("test.txt")
//     .toString()
//     .trim()
//     .split("\n")
//     .map((str) => str.replace("\r", ""));

class Queue {
    constructor(array) {
        this.array = array ? array : [];
        this.tail = array ? array.length : 0;
        this.head = 0;
    }

    enqueue(element) {
        this.array[this.tail++] = element;
    }

    dequeue() {
        if (this.tail === this.head) return -1;

        let ret = this.array[this.head];
        delete this.array[this.head];
        this.head += 1;

        return ret;
    }

    pop() {
        if (this.empty()) return -1;
        const result = this.array[--this.tail];
        return result;
    }

    size() {
        return Math.abs(this.head - this.tail);
    }

    empty() {
        return this.head === this.tail ? 1 : 0;
    }

    front() {
        if (this.empty()) return -1;
        return this.array[this.head];
    }

    back() {
        if (this.empty()) return -1;
        return this.array[this.tail - 1];
    }
}

const N = Number(input[0]);
input.splice(0, 1);

const q = new Queue();

for (let cmd of input) {
    if (cmd.split(" ").length === 2) {
        const [_, num] = cmd.split(" ").map(Number);
        q.enqueue(num);
    } else {
        switch (cmd) {
            case "pop":
                console.log(q.dequeue());
                break;
            case "size":
                console.log(q.size());
                break;
            case "empty":
                console.log(q.empty());
                break;
            case "front":
                console.log(q.front());
                break;
            case "back":
                console.log(q.back());
                break;
            default:
                break;
        }
    }
}
