import itertools

def is_prime(num):
    
    if num == 1 or num == 0: 
        return False

    for i in range(2, num):
        if i*i > num:
            break
        if num % i == 0:
            return False
    
    return True
        

def solution(numbers):
    
    sosus = []
    
    for i in range(1, len(numbers) + 1):
        arr = list(itertools.permutations(numbers, i))
        arr = [int(''.join(a)) for a in arr]
        sosus.extend(arr)
    
    sosus = list(set(sosus))

    answer = 0
    for n in sosus:
        if is_prime(n): 
            answer += 1
    
    return answer