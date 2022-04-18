function Train(number) {
    this.number = number;
    this.next = null;
}

function LinkedList() {
    this.head = null;
}

let input = [
    [4,7,1,10,6],
    [3,10,6,9,11,3,4],
    [5,8,7,3,4,1,2,7,10,7],
]

LinkedList.prototype.printNode = function () {
    for (let node = this.head; node != null; node = node.next) {
        process.stdout.write(`${node.number} -> `)
    }
    console.log("null")
}

function answer(trains) {
    let ll = new LinkedList();
    let prev = null;

    for (let train of trains) {
        let node = new Train(train);
        if (prev === null) {
            ll.head = node;
        } else {
            prev.next = node;
        }
        prev = node;
    }

    return ll;
}

for (let trains of input) {
    answer(trains).printNode()
}