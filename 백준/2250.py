class Tree:
    def __init__(self, i, l, r, d):
        self.index = i
        self.left = l
        self.right = r
        self.depth = d
    
    def addNode(self, i, l, r, d):
        if self.index == None or self.index == i:
            self.index = i
            self.depth = d
            self.left = Tree(l, None, None, self.depth + 1) if l != None else None
            self.right = Tree(r, None, None, self.depth + 1) if r != None else None
        else:
            flag = False
            if self.left != None:
                flag = self.left.addNode(i, l, r, d)