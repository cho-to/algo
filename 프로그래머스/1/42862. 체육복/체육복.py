def solution(n, lost, reserve):
    
    both = list(set(lost).intersection(set(reserve)))
    
    for b in both:
        lost.remove(b)
        reserve.remove(b)
    
    lost.sort()
    reserve.sort()
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n - len(lost)