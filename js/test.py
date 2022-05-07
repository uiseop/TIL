import heapq
from tabnanny import check

def checkRoutes(check_graph, results):
    for root, result in results:
        visited = [False for _ in range(1, len(check_graph) + 1)]
        node = []
        for key, value in result.items():
            if value == 0:
                visited[key] = True
            elif value != float("inf"):
                node.append(value)
    return results
    

def dijkstra(n, graph, start, summits, gates):
    results = []
    print("Graph: ", graph)

    for summit in summits:
        distances = {node: float("inf") for node in range(1, n+1)}
        distances[start] = 0
        
        
        queue = []
        heapq.heappush(queue, [distances[start], start])
        while queue:
            current_distance, current_destination = heapq.heappop(queue)
            if distances[current_destination] < current_distance: # 기존에 있는 거리보다 길면, 볼 필요도 없음
                continue
            if graph.get(current_destination):
                for new_destination, new_distance in graph[current_destination].items():
                    if new_destination in summits and new_destination != summit: # 현재 탐색하는 산봉우리가 다른 산봉우리면, 볼 필요도 없음
                        
                        continue
                    if new_destination in gates and new_destination != start: # 현재 탐색하는 노드가 다른 출입구라면, 볼 필요도 없음
                        
                        continue
                    distance = current_distance + new_distance
                    if distance < distances[new_destination]:
                        distances[new_destination] = distance
                        heapq.heappush(queue, [distance, new_destination])
        
        results.append([summit, distances])
    print("results: ", results)
    return results

def solution(n, paths, gates, summits):
    answer = []
    graph = {}
    check_graph = {}
    for frm, to, weight in paths:
        if graph.get(frm):
            graph[frm][to] = weight
            check_graph[frm][to] = weight
        else:
            graph[frm] = {
                to: weight
            }
            check_graph[frm] = {
                to: weight
            }
        if graph.get(to):
            check_graph[to][frm] = weight
        else:
            check_graph[to] = {
                frm: weight
            }
    
    for start in gates:
        result = dijkstra(n, graph, start, summits, gates)
        result = checkRoutes(check_graph, result)
    
    return answer

solution(7,[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],[1],[2, 3, 4])

def solution(alp, cop, problems):
    answer = 0
    t_alp, t_cop = problems[-1][0], problems[-1][1]
    n_alp = alp
    n_cop = cop
    diff_a = 0
    diff_c = 0
    for problem in problems:
        diff_a = max(problem[0] - alp, diff_a)
        diff_c = max(problem[1] - cop, diff_c)
    
    # while diff_a > 0 and diff_c > 0:
    if diff_a > diff_c:
        sorted(problems, key=lambda x:x[0])
    else:
        sorted(problems, key=lambda x:x[1])
    print(problems)

    return answer

solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])