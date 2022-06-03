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


# tree = Tree()
binary_search_tree = []

while True:
    try:
        num = int(input())
        # tree.insert(num)
        binary_search_tree.append(num)
    except:
        break


def post_order_print(left, right):
    if left > right: return
    middle = right + 1
    for i in range(left + 1, right + 1): # 현재 구간에서 루트 노드보다 큰 노드가 나오는 포인트 찾기
        if binary_search_tree[i] > binary_search_tree[left]:
            middle = i
            break
    
    post_order_print(left+1, middle-1)
    post_order_print(middle, right)
    print(binary_search_tree[left]) # 현재 노드의 value를 출력한다

post_order_print(0, len(binary_search_tree) - 1)

# tree.postOrder(tree.root)