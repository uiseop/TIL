import sys

input = sys.stdin.readline

n,c = map(int,input().split())

m = int(input())

box_infos = list(list(map(int,input().split())) for _ in range(m))

box_infos.sort(key=lambda x: [x[1],x[0]]) # 도착 일정을 기준으로 sort

cur_truck = [0 for _ in range(n+1)]

answer = 0

for frm, to, cnt in box_infos:
    # print(cur_truck, 'haha')
    if cur_truck[frm] == c:
        continue
    
    available = c - max(cur_truck[frm:to])
    if cnt >= available:
        answer += available
        for i in range(frm,to):
            cur_truck[i] += available
    else:
        answer += cnt
        for i in range(frm, to):
            cur_truck[i] += cnt

print(answer)