answer = 0

def solve(k, dungeons, went):
    global answer
    
    for i in range(0, len(dungeons)):
        dungeon = dungeons[i]
        if i in went:
            continue
        if k >= dungeon[0]:
            went.append(i)
            solve(k-dungeon[1], dungeons, went)
            went.pop()
        
    answer = len(went) if len(went) > answer else answer
    return

def solution(k, dungeons):
    
    solve(k, dungeons, [])
    
    return answer