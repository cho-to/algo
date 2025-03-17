def solution(s):
    answer = True
    stack = []
    for string in s:
        if string == ')':
            try:
                stack.pop()
            except:
                return False
        else:
            stack.append('(') 
    
    if len(stack) != 0:
        return False
    
    return True