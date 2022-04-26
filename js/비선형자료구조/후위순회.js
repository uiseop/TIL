const input = [
    "ABC",
    "FBADCEGIH",
    "CBAEDFG"
]

function Node(value) {
    this.value = value;
    this.left = null;
    this.right = null;
}

function Tree() {
    this.root = null;
}

Tree.prototype.addNode = function(value) {
    this.root = this._addNode(this.root, value);
}

Tree.prototype._addNode = function(node, value) {
    if (!node) {
        node = new Node(value)
    } else if (node.value > value) {
        node.left = this._addNode(node.left, value)
    } else if (node.value <= value) {
        node.right = this._addNode(node.right, value)
    }
    return node;
}

Tree.prototype.postOrder = function(node, array) {
    if (node === null) {
        return
    }
    this.postOrder(node.left, array);
    this.postOrder(node.right, array);
    array.push(node.value);
}

function answer(str) {
    let str2arr = str.split("");
    const tree = new Tree();
    let result = [];
    for (let s of str2arr) {
        tree.addNode(s)
    }
    tree.postOrder(tree.root, result);
    return result
}

for (let str of input) {
    console.log(answer(str));
}