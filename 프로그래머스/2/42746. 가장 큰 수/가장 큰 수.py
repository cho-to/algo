def solution(numbers):
    numbers = [str(n) for n in numbers]
    numbers.sort(reverse=True, key=lambda x: x*3)
    
    if all(n=='0' for n in numbers):
        return '0'
    
    return ''.join(numbers)