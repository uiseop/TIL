from collections import deque


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None
    
    def _insertNode(self, node, value):
        if not node:
            node = Node(value)
        elif value <= node.value:
            node.left = self._insertNode(node.left, value)
        else:
            node.right = self._insertNode(node.right, value)
        return node
    
    def insert(self, value):
        self.root = self._insertNode(self.root, value)

    def preOrder(self, node):
        print(node.value)
        if node.left:
            self.preOrder(node.left)
        if node.right:
            self.preOrder(node.right)
    
    def postOrder(self, node):
        if node.left:
            self.postOrder(node.left)
        if node.right:
            self.postOrder(node.right)
        print(node.value)
    
    def inOrder(self, node):
        if node.left:
            self.inOrder(node.left)
        print(node.value)
        if node.right:
            self.inOrder(node.right)

    def levelOrder(self):
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)



tree = Tree()

nums = [5,4,1,2,3,6,3]

for num in nums:
    tree.insert(num)

tree.levelOrder()