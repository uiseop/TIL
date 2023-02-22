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