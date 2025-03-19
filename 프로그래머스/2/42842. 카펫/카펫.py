def solution(brown, yellow):
    
    total = brown + yellow
    
    for i in range(2, total):
        if i*i > total:
            break
        if total % i == 0:
            a = i
            b = total // a
            if (a - 2)*2 + b*2 == brown:
                return [b, a]
    
    answer = []
    return answer