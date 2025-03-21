from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    orig_count = defaultdict(int)
    for idx in range(len(want)):
        orig_count[want[idx]] = number[idx]
    
    for idx, dsc in enumerate(discount):
        count = defaultdict(int)
        end = len(discount) if idx + 10 > len(discount) else idx + 10
        for j in range(idx, end):
            count[discount[j]] += 1
        
        ok = True
        for key, value in orig_count.items():
            if count[key] < orig_count[key]:
                ok = False
        
        if ok: answer += 1
                
        
        
    return answer