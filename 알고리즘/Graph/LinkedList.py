# 파이썬에서는 prototype을 선언하지 않고 객체지향 언어이기때문에 Class를 선언한다.
# 때문에 Class를 만들기 위해서는 __init__ (self): 라는 생성자 함수가 필수적으로 필요하고, 이에 따른 자료구조를 생성하면 된다.
# 그래프도 마찬가지로 구현하면 되겠다. 가령

# def __init__(self):
#     self.items = {}

# def addVertex (self, vertext):
#     self.items[vertext] = {}
# 위의 코드처럼 작성하면 된다. 그냥 자바스크립트랑 똑같다. 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        cur = self.head
        if not cur:
            self.head = Node(data)
            return
        while cur.next:
            cur = cur.next
        cur.next = Node(data)
    
    def print_all (self):
        cur = self.head
        if not cur:
            print("Linked List is Empty")
            return None
        while cur:
            cur = cur.next
    
    def get_node (self, index):
        cnt = 0
        node = self.head
        if not node:
            return
        while (not node and cnt < index):
            cnt += 1
            node = node.next
        return node

ll = LinkedList()
