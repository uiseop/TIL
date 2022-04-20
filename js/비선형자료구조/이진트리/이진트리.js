function Node(value) {
    this.value = value;
    this.left = null;
    this.right = null;
}

function BionaryTree() {
    this.root = null;
}

BionaryTree.prototype._insertNode = function (node, value) {
    if (node === null) {
        node = new Node(value);
    } else if (value < node.value) {
        // root노드보다 작으면 left
        node.left = this._insertNode(node.left, value);
    } else if (value >= node.value) {
        // root노드보다 크면 right
        node.right = this._insertNode(node.right, value);
    }
    return node;
};

BionaryTree.prototype.insert = function (value) {
    this.root = this._insertNode(this.root, value);
};

const tree = new BionaryTree();

tree.insert("A")
tree.insert("B")
tree.insert("C")
tree.insert("D")
tree.insert("E")
tree.insert("F")
tree.insert("G")


console.log(tree)

/* output
BionaryTree {
  root: Node {
    value: 'A',
    left: null,
    right: Node { value: 'B', left: null, right: [Node] }
  }
}
*/