def solution(m, n, puddles):
    route = [[0 for _ in range(m)] for _ in range(n)]
    for p in puddles:
        route[p[1]-1][p[0]-1] = -1
    
    prev = 1
    for i in range(m):
        if route[0][i] == -1:
            prev = -1
        route[0][i] = prev
        
    prev = 1
    for i in range(n):
        if route[i][0] == -1:
            prev = -1
        route[i][0] = prev
    
    for i in range(1, n):
        for j in range(1, m):
            if route[i][j] == -1:
                continue
            up = 0 if route[i-1][j] == -1 else route[i-1][j]
            left = 0 if route[i][j-1] == -1 else route[i][j-1]
            route[i][j] = up + left
    

    return route[n-1][m-1] % 1_000_000_007