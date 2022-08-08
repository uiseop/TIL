from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

cnt = 0
visitCnt = 0
in_order_list = [] 

class Node:
    def __init__(self,root,left,right):
        self.root = root
        self.left = left
        self.right = right
    
def similarInOrder(node):
    global cnt, visitCnt
    if node.left:
        cnt += 1
        similarInOrder(tree[node.left])
        cnt += 1
    visitCnt += 1
    if node.right:
        cnt += 1
        similarInOrder(tree[node.right])
        if visitCnt == n: return
        cnt += 1


n = int(input())
tree = defaultdict(Node)
for _ in range(n):
    a,b,c = map(int,input().split())
    if b == -1: b = 0
    if c == -1: c = 0
    tree[a] = Node(a,b,c)

# def isEnd(node):
#     if node.root == right_leaf:
#         return True
#     return False 


# def find_leaf(root):
#     res = root
#     if tree[root].right:
#         res = find_leaf(tree[root].right)
#     elif tree[root].left:
#         res = find_leaf(tree[root].left)
#     return res

# right_leaf = find_leaf(1)

similarInOrder(tree[1])
print(cnt)