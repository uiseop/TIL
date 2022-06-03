import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def _insertNode(self, node, value):
        if not node:
            node = Node(value)
        elif value < node.value:
            node.left = self._insertNode(node.left, value)
        elif value > node.value:
            node.right = self._insertNode(node.right, value)
        return node
    
    def insert(self, value):
        self.root = self._insertNode(self.root, value)

    def postOrder(self,node):
        if node.left:
            self.postOrder(node.left)
        if node.right:
            self.postOrder(node.right)
        print(node.value)


tree = Tree()

while True:
    try:
        num = int(input())
        tree.insert(num)
    except:
        break
    
tree.postOrder(tree.root)