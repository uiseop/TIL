def getRoutes(routes):
    bits = [0] * 17
    for route in routes:
        bits[route] = 1
    return ''.join(map(str,(bits)))

def solution(info, edges):
    answer = []
    visited = [False for _ in range(len(info))]
    visited[0] = True
    bit_set = set()
    def dfs(sheep, wolf, routes):
        bits = getRoutes(routes)
        if bits in bit_set: return
        bit_set.add(bits)
        if sheep > wolf:
            answer.append(sheep)
        else: return # 늑대가 양을 모두 잡아먹어버리기 때문에 더이상 1마리씩 가져오는걸로는 양을 가져오지 못함. 때문에 바로 함수를 return(종료)
        
        for parent, child in edges:
            isWolf = info[child]
            if visited[parent] and not visited[child]:
                visited[child] = True
                if isWolf:
                    dfs(sheep, wolf+1, routes + [child])
                else:
                    dfs(sheep+1, wolf, routes + [child])
                visited[child] = False
    dfs(1,0, [0])
    return max(answer)

solution([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16]])