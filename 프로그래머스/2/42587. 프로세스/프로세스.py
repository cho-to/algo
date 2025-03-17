from collections import deque

def solution(priorities, location):
    count = 0
    dq = deque((i, q) for i, q in enumerate(priorities))
    
    while dq:
        n = dq.popleft()
        
        if any(n[1]<q[1] for q in dq):
            dq.append(n)
            continue
        count += 1
        
        if n[0] == location:
            return count
        
    
    