def solution(prices):
    stack = []
    answer = []
    
    prices = [(p, idx) for idx, p in enumerate(prices)]
    prices.reverse()
    count = 0

    for price in prices:
        
        while len(stack) != 0 and stack[-1][0] >= price[0]:
            stack.pop()
            
        if len(stack) == 0:
            answer.append(count)
        else:
            answer.append(stack[-1][1] - price[1])
        
        count += 1
        stack.append(price)
    
    answer.reverse()
    return answer