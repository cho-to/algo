from collections import deque

def solution(people, limit):
    
    answer = 0
    
    people.sort()
    people = deque(people)
    
    while len(people) != 0:
        if len(people) != 1 and people[0] + people[-1] <= limit:
            answer += 1
            people.popleft()
            people.pop()
        else:
            answer += 1
            people.pop()
            
    
    return answer