from collections import deque

def solution(tickets):
    answer = []
    
    q = deque([])
    
    for idx, t in enumerate(tickets):
        if t[0] == 'ICN':
            q.append((t, [(t, idx)])) # current ticket, route
    
    while q:
        k, route = q.popleft()
        
        if len(route) == len(tickets):
            answer.append(route)
            continue
        
        for idx, t in enumerate(tickets):
            if k[1] == t[0]:
                if any(idx == r[1] for r in route):
                    continue
                
                next_route = []
                for r in route:
                    next_route.append(r)
                next_route.append((t, idx))
                q.append((t, next_route))
                
    final_route = []
    for route in answer:
        arr = []
        for r in route:
            arr.append(r[0][0])
        arr.append(route[-1][0][1])
        final_route.append(arr)
    
    final_route.sort(key=lambda x: ''.join(x))
    
    return final_route[0]