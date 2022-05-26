import sys
input = sys.stdin.readline

def root(i):
    if data[i]<0:return i
    data[i] = root(data[i])
    return data[i]

def union(a,b):
    a,b = map(root,(a,b))
    if a == b: return None
    data[b] = a

N = int(input())
M = int(input())
data = [-1]*N

for i in range(N):
    adj = list(map(int,input().split()))
    for j in range(i+1,N):
        if adj[j]:union(i,j)

plan = list(map(int,input().split()))
start = root(plan[0]-1)
for p in plan[1:]:
    if start !=root(p-1):
        print("NO")
        break
else:
    print("YES")

# Union-Find로 결국 시작점과 다음 지점의 root가 같아야
# 그래프가 연결되어있다는 뜻 이기 때문에 index로 접근하는 이 방법이
# 약 3배 가량 빠르다. union-find는 그래프가 연결되어있는지 확인하는데 사용
# 때문에 갈 수 있는지 없는지는 연결되어 있는지 아닌지를 확인하는게
# 빠르다.