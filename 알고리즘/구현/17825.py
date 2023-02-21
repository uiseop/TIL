class Node:
    def __init__(self, value, red=None, blue=None,):
        self.value = value
        self.blue = blue
        self.red = red
    def addRed(self, red):
        self.red = red
    def addBlue(self, blue):
        self.bule = blue

nodes = [
Node(2),#0
Node(4),
Node(6),
Node(8),
Node(10),#4
Node(13),#5
Node(16),
Node(19),#7
Node(12),#8
Node(14),
Node(16),
Node(18),
Node(20),#12
Node(22),#13
Node(24),
Node(25),#15
Node(22),#16
Node(24),
Node(26),
Node(28),
Node(30),#20
Node(28),#21
Node(27),
Node(26),#23
Node(32),#24
Node(34),
Node(36),
Node(38),#27
Node(30),#28
Node(35),
Node(40),#30
Node('도착'),
Node('시작')]

nodes[4].addRed(nodes[8])
nodes[4].addBlue(nodes[5])
nodes[7].addRed(nodes[15])
nodes[15].addRed(nodes[28])
nodes[30].addRed(nodes[31])
nodes[12].addRed(nodes[16])
nodes[12].addBlue(nodes[13])
nodes[20].addRed(nodes[24])
nodes[20].addBlue(nodes[21])
nodes[23].addRed(nodes[15])
nodes[27].addRed(nodes[30])
nodes[-1].addRed(nodes[0])

for i in range(0, 4):
    nodes[i].addRed(nodes[i+1])

for i in range(5,7):
    nodes[i].addRed(nodes[i+1])

for i in range(8, 12):
    nodes[i].addRed(nodes[i+1])

for i in range(13,15):
    nodes[i].addRed(nodes[i+1])

for i in range(16,20):
    nodes[i].addRed(nodes[i+1])

for i in range(21,23):
    nodes[i].addRed(nodes[i+1])

for i in range(24,27):
    nodes[i].addRed(nodes[i+1])

for i in range(28, 30):
    nodes[i].addRed(nodes[i+1])

horse = [nodes[-1] for _ in range(4)]
n = list(map(int,input().split()))
answer = 0

def dfs(tot, nid):
    global answer
    if nid == 10:
        answer = max(answer, tot)
        return
    for hid in range(4):
        memo = horse[hid]
        h = horse[hid]
        cnt = n[nid]
        if h and h.value != 'x' and h.value != '도착':
            if h.blue:
                h = h.blue
                cnt -= 1
            for _ in range(cnt):
                if not h.red:
                    break
                h = h.red
            else:
                n_tot = tot
                if str(type(h.value)) != "<class 'str'>":
                    n_tot += h.value
                if horse.count(h) > 1:
                    horse[hid].value = 'x'
                horse[hid] = h
                dfs(n_tot,nid+1)
                horse[hid] = memo

dfs(0, 0)
print(answer)
