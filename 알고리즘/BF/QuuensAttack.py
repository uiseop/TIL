from collections import defaultdict, deque

dir = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

def solve(n,k,r_q,c_q,obstacles):
    # Write your code here
    r_q -= 1
    c_q -= 1

    obs_dict = defaultdict(bool)
    
    for r_o, c_o in obstacles:
        r_o -= 1
        c_o -= 1
        obs_dict[(r_o, c_o)] = True
    
    answer = 0
    q = deque()
    
    for d in range(8):
        dr,dc = dir[d][0], dir[d][1]
        nr,nc = r_q + dr, c_q + dc
        if 0 <= nr < n and 0 <= nc < n and not obs_dict[(nr, nc)]:
            q.append([nr,nc,d])
            answer += 1
    
    while q:
        r,c,d = q.popleft()
        dr,dc = dir[d][0], dir[d][1]
        nr,nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and not obs_dict[(nr, nc)]:
            q.append([nr,nc,d])
            answer += 1
    return answer

# obs = list(map(int,input().split()) for _ in range(3)))
obs = []
print(solve(100000,0,4187,5068, obs))
