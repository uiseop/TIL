class Tree:
    def __init__(self, i, l, r):
        self.index = i
        self.left = l
        self.right = r
    
    def addNode(self, i, l, r):
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None
            return True
        
        else:
            flag = False
            if self.left != None:
                flag = self.left.addNode(i, l, r)
            
            if flag == False and self.right != None:
                flag = self.right.addNode(i, l, r)
            
            return flag

def preorder(T):
    result = []

    result.append(T.index)
    if T.left != None:
        result += preorder(T.left)
    if T.right != None:
        result += preorder(T.right)
    
    return result

def inorder(T):
    result = []

    if T.left != None:
        result += inorder(T.left)
    result += T.index
    if T.right != None:
        result += inorder(T.right)
    
    return result

def postorder(T):
    result = []

    if T.left != None:
        result += postorder(T.left)
    if T.right != None:
        result += postorder(T.right)
    result += T.index

    return result

myTree = Tree(None, None, None)

for _ in range(int(input())):
    i,l,r = map(str,input().split())
    if l == '.':
        l = None
    if r == '.':
        r = None

    myTree.addNode(i, l, r)

print(''.join(preorder(myTree)))
print(''.join(inorder(myTree)))
print(''.join(postorder(myTree)))