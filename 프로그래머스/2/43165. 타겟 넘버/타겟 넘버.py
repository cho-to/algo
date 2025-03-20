answer = 0

def solve(idx, numbers, target, total):
    global answer
    
    if idx == len(numbers):
        if total == target:
            answer += 1
        return
    
    for i in [-1, 1]:
        total += i * numbers[idx]
        solve(idx+1, numbers, target, total)
        total -= i * numbers[idx]

def solution(numbers, target):
    
    solve(0, numbers, target, 0)
    
    return answer