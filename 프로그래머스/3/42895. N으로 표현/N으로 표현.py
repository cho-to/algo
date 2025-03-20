def solution(N, number):
    answer = [-1] * 32001
        
    prev = [[] for _ in range(9)]
    prev[1].append(N)
    answer[N] = 1
    
    for i in range(2, 9):
        arr = set([])
        arr.add(int(str(N)*i))
        
        for j in range(1, i//2 + 1):
            for n1 in prev[j]:
                for n2 in prev[i-j]:
                    arr.add(n1*n2)
                    if n2 != 0:
                        arr.add(n1//n2)
                    if n1 != 0:
                        arr.add(n2//n1)
                    arr.add(n1-n2)
                    arr.add(n2-n1)
                    arr.add(n1+n2)
        
        for n in list(arr):
            if n < 1 or n > 32000:
                continue
            answer[n] = i if answer[n] == -1 else answer[n]
        
        prev[i].extend(list(arr))
    
    
    return answer[number]