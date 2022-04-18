function Node(data) {
    this.data = data;
    this.next = null;
}

function LinkedList() {
    this.head = null;
    this.length = 0;
}

LinkedList.prototype.size = function () {
    return this.length;
};

LinkedList.prototype.isEmpty = function () {
    return this.length === 0;
};

LinkedList.prototype.printNode = function () {
    for (let node = this.head; node != null; node = node.next) {
        process.stdout.write(`${node.data} -> `);
    }
    console.log("null");
};

LinkedList.prototype.append = function (data) {
    let node = new Node(data);
    let current = this.head;

    if (this.head === null) {
        this.head = node;
    } else {
        while (current.next != null) {
            current = current.next;
        }
        current.next = node;
    }

    this.length += 1;
};

LinkedList.prototype.insert = function (data, index = 0) {
    if (index < 0 || index > this.length) {
        console.log("해당 인덱스에는 넣을 수 없습니다.")
        return false
    }

    let node = new Node(data);
    let current = this.head;
    let idx = 0;
    let prev;
    if (index === 0) {
        node.next = current;
        this.head = node;
    }else {
        while (index !== idx) {
            prev = current;
            current = current.next;
            idx += 1;
        }
        prev.next = node;
        node.next = current;
    }
    this.length += 1
    return true

}

LinkedList.prototype.remove = function(value) {
    let current = this.head;
    let prev;
    this.length -= 1;

    if (current.data === value) {
        this.head = current.next;
        return current.data;
    }
    while (current.data != value && current.next != null) {
        prev = current;
        current = current.next;
    }
    if (current.data != vaule) {
        console.log(`지우고자 하는 ${value}가 없습니다.`)
        return null;
    }
    prev.next = current.next;
    return current.data;
}

let li = new LinkedList();
li.append(1);
li.append(10);
li.append(100);
li.append(1000);

li.printNode();

li.insert(333, 2)

li.printNode();


/* output
1 -> 10 -> 100 -> 1000 -> null

1 -> 10 -> 333 -> 100 -> 1000 -> null
*/
