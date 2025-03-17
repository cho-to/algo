def solution(clothes):
    answer = 0
    dic = {}
    for cloth, typ in clothes:
        if typ in dic:
            dic[typ] += 1
        else:
            dic[typ] = 1
    
    answer = 1
    for key, value in dic.items():
        answer *= (value + 1)
    
    return answer - 1
    