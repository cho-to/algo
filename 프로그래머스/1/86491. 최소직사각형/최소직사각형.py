def solution(sizes):
    answer = 0
    garo = []
    sero = []
    
    for idx, s in enumerate(sizes):
        if s[0] < s[1]:
            sizes[idx] = [s[1], s[0]]

    for s in sizes:
        garo.append(s[0])
        sero.append(s[1])
            
            
    return max(garo) * max(sero)