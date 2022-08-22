class stack:
    def __init__(self,size):
        self.size = size
        self.items = []
    
    def isFull(self):
        if len(self.items) == self.size:
            return True
        return False
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def push(self, data):
        if not self.isFull():
            self.items.append(data)
            return f'{data} is pushed'
        return 'Stack is Full'
    
    def pop(self):
        if not self.isEmpty():
            item = self.items.pop()
            return f'{item} is poped'
        return 'Stack is Empty'
    
    def printStack(self):
        if not self.isEmpty():
            for item in self.items:
                print(item, end=' ')
            return
        return 'Stack is Empty'
    
stack1 = stack(10)

print(stack1.pop())
print(stack1.printStack())

print(stack1.push(5))
print(stack1.push(4))
print(stack1.push(3))
print(stack1.push(2))

for i in range(8):
    print(stack1.push(i))

        
print(stack1.pop())
stack1.printStack()