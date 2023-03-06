import sys

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    players = []
    for _ in range(11):
        players.append(list(map(int,input().split())))
    isSelected = [False for _ in range(11)]
    positionPossible = [[] for _ in range(11)]

    for pid in range(11):
        player = players[pid]
        for p in range(11):
            if player[p]:
                positionPossible[p].append(pid)

    def backtrack(i, total):
        if i == 11:
            return total
        
        result = 0
        for pid in positionPossible[i]:
            if isSelected[pid]: continue
            player = players[pid]
            isSelected[pid] = True
            result = max(result, backtrack(i+1, total + player[i]))
            isSelected[pid] = False

        return result
    
    print(backtrack(0, 0))
