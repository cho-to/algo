from collections import deque

def solution(begin, target, words):
    
    word_len = len(begin)
    visited = {}
    visited[begin] = 0
    for word in words:
        visited[word] = 0
    q = deque([])
    q.append(begin)
    
    if target not in words:
        return 0
    
    while q:
        n = q.popleft()
        
        if n == target:
            return visited[n]
        
        for i in range(word_len):
            for word in words:
                if n[:i] == word[:i] and n[i+1:] == word[i+1:] and n != word:
                    if visited[word] == 0:
                        visited[word] = visited[n] + 1
                        q.append(word)
        
    
    return 0