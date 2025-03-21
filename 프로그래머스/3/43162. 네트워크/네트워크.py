from collections import deque

def solution(n, computers):
    
    answer = 0
    
    visited = [False] * n
    
    for i in range(n):
        if visited[i]: continue
        
        q = deque([])
        q.append(i)
        
        while q:
            k = q.popleft()
            if visited[k]: continue
            for j in range(n):
                if computers[k][j] and k != j:
                    q.append(j)
            visited[k] = True
        
        answer += 1
        
    return answer