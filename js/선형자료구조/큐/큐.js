function Queue(array) {
    this.array = array ? array : [];
    this.tail = array ? array.length : 0;
    this.head = 0;
}

Queue.prototype.enqueue = function (element) {
    return (this.array[this.tail++] = element);
};

Queue.prototype.dequeue = function () {
    if (this.tail === this.head) return undefined;

    let ret = this.array[this.head];
    delete this.array[this.head];
    this.head += 1;

    return ret;
};

function Queue2(array) {
    this.array = array ? array : [];
}

Queue2.prototype.enqueue = function (element) {
    return this.array.push(element);
};

Queue2.prototype.dequeue = function () {
    return this.array.shift();
};

let new_q = new Queue();
let q = new Queue2();

const count = 100000;

// 결과

function benchmark(queue, enqueue) {
    let start = Date.now();
    for (let i = 0; i < count; i++) {
        enqueue ? queue.enqueue() : queue.dequeue(); // 1이면 enqueue, 0이면 dequeue
    }
    return Date.now() - start;
}

console.log("Enque new_q: " + benchmark(new_q, 1) + "ms")
console.log("Enque q: " + benchmark(q, 1) + "ms")


console.log("Dequeue new_q: " + benchmark(new_q, 0) + "ms")
console.log("Dequeue q: " + benchmark(q, 0) + "ms")

/*
Enque new_q: 10ms
Enque q: 9ms

Dequeue new_q: 13ms
Dequeue q: 1545ms

약 100배 차이가 남을 확인
*/