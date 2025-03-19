def solution(number, k):
    answer = ''
    stack = []
    cnt = 0
    
    for idx, n in enumerate(number):
        n = int(n)
        while stack and stack[-1] < n and cnt != k:
            stack.pop()
            cnt += 1
        
        if idx == len(number) -1 and stack and stack[-1] > n and cnt != k:
            continue
            
        stack.append(n)
        
        
    return ''.join(list(map(str, stack)))