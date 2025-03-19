from collections import deque

def solution(name):
    
    ud_total = 0
    for n in name:
        ud_total += min(ord(n)-ord('A'), 26 - (ord(n)-ord('A')))
   

    lr_total = 0
    
    visited = [0] * len(name)
    for idx, n in enumerate(name):
        if n == 'A': visited[idx] = 1
    
    q = deque([])
    q.append([0, 0, visited.copy()]) # location, count
    
    while q:
        q_ = q.popleft()

        x, cnt, vis = q_[0], q_[1], q_[2]
        vis[x] = 1
        if vis.count(1) == len(name):
            lr_total = cnt
            break
        
        left = len(name) - 1 if x - 1 < 0 else x - 1
        right = 0 if x + 1 == len(name) else x + 1
        for nx in [ left, right ]:
            q.append([nx, cnt + 1, vis.copy()])
    
    return ud_total + lr_total