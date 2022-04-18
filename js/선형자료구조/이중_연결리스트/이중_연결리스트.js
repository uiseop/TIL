function Node(data) {
    this.data = data;
    this.next = null;
    this.prev = null;
}

function DoubleLinkedList() {
    this.head = null;
    this.tail = null;
    this.length = 0;
}

DoubleLinkedList.prototype.size = function () {
    return this.length;
};

DoubleLinkedList.prototype.isEmpty = function () {
    return this.length === 0;
};

DoubleLinkedList.prototype.printNode = function () {
    let current = this.head;
    while (current.data !== null && current.next !== null) {
        current = current.next;
        process.stdout.write(`${current.data} -> `);
    }
    console.log("null");
};

DoubleLinkedList.prototype.printNodeReverse = function () {
    let current = this.tail;
    process.stdout.write("null <- ");
    while (current.data !== null && current.prev !== null) {
        current = current.prev;
        process.stdout.write(`${current.data} <- `);
    }
    console.log("tail");
};

DoubleLinkedList.prototype.append = function (value) {
    let node = new Node(value);
    if (this.head === null) {
        this.head = node;
        this.tail = node;
    } else {
        this.tail.next = node;
        node.prev = this.tail;
        this.tail = node;
    }

    this.length += 1;
};

DoubleLinkedList.prototype.insert = function(value, index = 0) {
    if (index < 0 || index > this.length) {
        return false
    }
    let node = new Node(value);
    if (this.length / 2 <= index) { // 중간보다 작으면 head -> 반
        let current = this.head;
        if (this.head === null) {
            this.head = node;
            this.tail = node;
        } else {
            node.next = current;
            current.prev = node;
            this.head = node
        }
    } else { // tail -> 반

    }
}

DoubleLinkedList.prototype.remove = function(value) {
    let head = this.head;
    let tail = this.tail;
    let isEnd = false;
    while (!isEnd && head !== tail) {
        if (head.data === value) {
            isEnd = true
        } else {
            head = head.next;
        }

        if (tail.data === value) {
            isEnd = true
        } else {
            tail = tail.prev;
        }
    }

    if (!isEnd) {
        console.log("지울 수 없습니다.")
        return false
    } else {
        if (head.data === value) {
            head.prev.next = head.next;
            head.next.prev = head.prev;
        } else {
            tail.prev.next = tail.next;
            tail.next.prev = tail.prev;
        }
    }

    this.length -= 1;
}

let dll = new DoubleLinkedList();

dll.append(1);
dll.append(10);
dll.append(100);
dll.append(1000);

dll.printNode();

dll.remove(100)

dll.printNode();

dll.printNodeReverse();

/* output
10 -> 100 -> 1000 -> null
10 -> 1000 -> null
null <- 100 <- 10 <- 1 <- tail
*/