def solution(arr):
    answer = []
    prev = -1
    for n in arr:
        if prev != n:
            answer.append(n)
        prev = n
        
    return answer