import heapq

def solution(scoville, K):
    foods = scoville
    heapq.heapify(foods)
    count = 0
    
    while len(foods) != 1:
        if foods[0] >= K:
            break
        first = heapq.heappop(foods)
        second = heapq.heappop(foods)
        heapq.heappush(foods, first + second*2)
        
        count += 1
    
    if foods[0] < K:
        return -1
    else:
        return count