n = int(input())

ipt = []

for _ in range(n):
    ipt.append(list(map(int, input().split())))


def solution(triangle):
    route = []
    for trg in triangle:
        route.append(trg.copy())
    
    for idx1, trg in enumerate(route):
        if idx1 == len(route) - 1:
            break
        for idx2, t in enumerate(trg):
            route[idx1+1][idx2] = max(route[idx1+1][idx2], triangle[idx1+1][idx2] + t)
            route[idx1+1][idx2+1] = max(route[idx1+1][idx2+1], triangle[idx1+1][idx2+1] + t)
        
    return max(route[-1])

print(solution(ipt))