words = []

def solve(word):
    
    if word:
        words.append(''.join(word))
    
    if len(word) == 5:
        return
    
    for i in ['A', 'E', 'I', 'O', 'U']:
        word.append(i)
        solve(word)
        word.pop()


def solution(word):
    
    solve([])
    
    words_list = list(set(words))
    words_list.sort()
    
    return words_list.index(word) + 1