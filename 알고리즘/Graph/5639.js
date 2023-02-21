let fs = require("fs");
// let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
let input = fs
    .readFileSync("test.txt")
    .toString()
    .trim()
    .split("\n")
    .map((str) => str.replace("\r", ""));

const nums = input.map(Number);

function Tree() {
    this.key = null;
    this.left = null;
    this.right = null;
}

Tree.prototype.addVertex = function (vertex) {
    let root = this.key;
    if (!root) {
        this.key = vertex;
        return;
    }
    if (vertex < root) {
        if (!this.left) {
            const leftTree = new Tree();
            leftTree.key = vertex;
            this.left = leftTree;
            return;
        }
        return this.left.addVertex(vertex);
    } else {
        if (!this.right) {
            const rightTree = new Tree();
            rightTree.key = vertex;
            this.right = rightTree;
            return;
        }
        return this.right.addVertex(vertex);
    }
};

Tree.prototype.preorder = function () {
    if (!this.key) return;
    console.log(this.key);
    if (this.left) {
        this.left.preorder();
    }
    if (this.right) {
        this.right.preorder();
    }
};

Tree.prototype.postorder = function () {
    if (this.left) {
        this.left.postorder();
    }
    if (this.right) {
        this.right.postorder();
    }
    if (this.key) {
        console.log(this.key);
    }
};

const T = new Tree();

// nums.forEach((num) => T.addVertex(num))

// T.postorder()

class Node {
    constructor(value, left, right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    print() {
        return this.value;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    insert(val) {
        let value = new Node(val, null, null);
        if (this.root === null) {
            this.root = value;
        } else {
            let current = this.root;
            let parent;
            while (true) {
                parent = current;
                if (val < current.value) {
                    current = current.left;
                    if (current === null) {
                        parent.left = value;
                        break;
                    }
                } else {
                    current = current.right;
                    if (current === null) {
                        parent.right = value;
                        break;
                    }
                }
            }
        }
    }
}

let binarySearchTree = new BinarySearchTree();

let curTime = Date.now();
for (let i = 0; i < 10 ** 4; i++) {
    T.addVertex(i);
}

let endTime = Date.now();
console.log("My Tree: ", endTime - curTime);

cur2Time = Date.now();
for (let i = 0; i < 10 ** 4; i++) {
    binarySearchTree.insert(i);
}
end2Time = Date.now();
console.log("Your Tree:", end2Time - cur2Time);
