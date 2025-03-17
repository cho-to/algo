from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge_ing = deque([])
    bridge_wait = deque(t for t in truck_weights)
    
    sec = 0
    now_weight = 0
    
    while True:
        if not bridge_ing and not bridge_wait: break

        sec += 1
        
        # 트럭 건너게 해주기
        pop = False
        for idx, truck in enumerate(bridge_ing):
            bridge_ing[idx] = (truck[0], truck[1] + 1)
            if truck[1] + 1 == bridge_length: pop=True
        if pop: 
            truck = bridge_ing.popleft()
            now_weight -= truck[0]
        
        # 대기 중이던 트럭 올리기
        if bridge_wait:
            truck = bridge_wait[0]
            if now_weight + truck > weight:
                continue
            truck = bridge_wait.popleft()
            bridge_ing.append((truck, 0))
            now_weight += truck
        
    
    return sec