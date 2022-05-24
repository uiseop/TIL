function Node(data) {
    this.data = data;
    this.prev = null;
    this.next = null;
}

function Dequeu() {
    this.head = null;
    this.tail = null;
}

Dequeu.prototype.unshift = function (data) { // enqueue
    const node = new Node(data);
    if (!this.head) {
        this.head = node;
        this.tail = node;
    } else {
        this.head.prev = node;
        node.next = this.head;
        this.head = node;
    }
}

Dequeu.prototype.push = function (data) {
    const node = new Node(data);
    if (!this.tail) {
        this.head = node;
        this.tail = node;
    } else {
        this.tail.next = node;
        node.prev = this.tail;
        this.tail = node;
    }
}

Dequeu.prototype.shift = function () { // dequeue
    const result = this.head;
    if (!result) return null;
    if (!this.head.next) {
        this.head = null;
        this.tail = null;
    } else {
        this.head = this.head.next;
        this.head.prev = null; // head가 next node로 바뀌었으니 node는 prev와 next를 갖는데, prev를 비워줘야지
    }
    return result.data;
}

Dequeu.prototype.pop = function () {
    const result = this.tail;
    if (!result) return null;
    if (!this.tail.prev) {
        this.head = null;
        this.tail = null;
    } else {
        this.tail = this.tail.prev;
        this.tail.next = null;
    }
    return result.data;
}