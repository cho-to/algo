def solution(progresses, speeds):
    total = []
    answer = []
    count = 0
    
    length = len(progresses)

    for i in range(0, length):
        if (100 - progresses[i]) % speeds[i] == 0:
            total.append((100 - progresses[i]) // speeds[i])
        else:
            total.append((100 - progresses[i]) // speeds[i] + 1)
    
    prev = total[0]
    
    for n in total:
        if prev >= n:
            count += 1
        else:
            answer.append(count)
            count = 1
            prev = n
    answer.append(count)
    
    return answer