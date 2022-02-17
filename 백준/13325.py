h = int(input())
# 포화 이진트리는 배열로 간단하게 표현할 수 있음. 각 자식노드는 부모노드 index*2, index*2 + 1에 위치하기 때문에
tree = list(map(int,input().split()))
node = [0] * (2**(h+1) - 2)

ans = 0

for i in range(h, 0, -1):
    for j in range(2**i -2, 2**(i+1) -2, 2):
        a,b = tree[j] + node[j], tree[j+1] + node[j+1]
        node[(j-2) // 2] = max(a,b)
        ans += max(a,b) - min(a,b)

print(ans + sum(tree))