def solution(citations):
    answer = -1
    h = -1
    
    citations.sort()
    length = len(citations)
    prev = -1
    
    for idx, c in enumerate(citations):
        if prev != c:
            while h != c:
                h += 1
                upper = length - idx
                if upper >= h:
                    answer = h if answer < h else answer
        
        prev = c
    
    return answer