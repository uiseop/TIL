import sys

input = sys.stdin.readline

n,k = map(int, input().split())

counters = []

for _ in range(n):
    counter = list(map(int, input().split()))
    counters.append(counter)

people = [[]]
kh = list(map(int, input().split()))
mh = list(map(int, input().split()))
people.append(kh)
people.append(mh)

points = [0, 0, 0]

pos = [i for i in range(n)]
# jw = [False for _ in range(n)]

answer = 0

def dfs(idx, p1, p2, cnt, pre=None): # 0 지우, 1 경희, 2 민호
    global answer
    if answer == 1:
        return
    if idx == 20 or points[0] == k:
        answer = 1
        return True
    if points[1] == k or points[2] == k:
        return False
    isChange = False
    if p1 > p2:
        p1,p2 = p2,p1
        isChange = True
    if p1 == 0:
        for i in pos:
            if i == pre:
                continue
            p2_got = people[p2][idx] - 1
            if counters[i][p2_got] == 2:
                points[0] += 1
                dfs(idx+1, p1, 1 if p2 != 1 else 2, i) 
                points[0] -= 1
            elif counters[i][p2_got] == 1:
                if isChange:
                    dfs(idx+1, p1, 1 if p2 != 1 else 2, i)
                else:
                    
                    dfs(idx+1, p2, 1 if p2 != 1 else 2, i)
            else:
                points[p2] += 1
                dfs(idx+1, p2, 1 if p2 != 1 else 2, i)
                points[p2] -= 1
    else:
        p1_got = people[p1][idx] - 1
        p2_got = people[p2][idx] - 1
        if counters[p1_got][p2_got] == 2:
            points[p1] += 1
            dfs(idx+1, p1, 0, pre)
            points[p1] -= 1
        elif counters[p1_got][p2_got] == 1:
            if isChange:
                dfs(idx+1, p1, 0, pre)
            else:
                dfs(idx+1, p2, 0, pre)
        else:
            points[p2] += 1
            dfs(idx+1, p2, 0, pre)
            points[p2] -= 1

dfs(0,0,1)
print(answer)