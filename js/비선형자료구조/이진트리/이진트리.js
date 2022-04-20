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

tree.insert("F")
tree.insert("B")
tree.insert("A")
tree.insert("D")
tree.insert("C")
tree.insert("E")
tree.insert("G")
tree.insert("I")
tree.insert("H")


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
const preOrder = [];
const inOrder = [];
const postOrder = [];
BionaryTree.prototype.preOrder = function(node) {
    
    if (node === null) {
        return;
    }
    preOrder.push(node.value);
    this.preOrder(node.left);
    this.preOrder(node.right);
}

BionaryTree.prototype.inOrder = function(node) {
    if(node === null) {
        return;
    }
    this.inOrder(node.left);
    inOrder.push(node.value);
    this.inOrder(node.right);
}

BionaryTree.prototype.postOrder = function(node) {
    if(node === null) {
        return;
    }
    this.postOrder(node.left);
    this.postOrder(node.right);
    postOrder.push(node.value);
}
tree.preOrder(tree.root)
tree.inOrder(tree.root)
tree.postOrder(tree.root)

console.log("preOrder result: ", preOrder.join("->"))
console.log("inOrder result: ", inOrder.join("->"))
console.log("postOrder result: ", postOrder.join("->"))