from collections import deque

def solution(maps):
    n, m = len(maps[0]), len(maps)
    
    visited = []
    for i in range(m):
        visited.append([-1]*n)
    
    q = deque([])
    q.append(((0, 0), 1)) # pos, count(길이)
    visited[0][0] = 1 
    
    nx = [1, 0, -1, 0]
    ny = [0, 1, 0, -1]
    
    while q:
        pos, cnt = q.popleft()
        dx, dy = pos
        
        if dx == m-1 and dy == n-1:
            return cnt
        
        for i in range(0, 4):
            x = dx + nx[i]
            y = dy + ny[i]
            if x < 0 or y < 0 or x >= m or y >= n:
                continue
            if maps[x][y] == 1 and visited[x][y] == -1:
                visited[x][y] = cnt+1
                q.append(((x, y), cnt+1))
    
    return -1