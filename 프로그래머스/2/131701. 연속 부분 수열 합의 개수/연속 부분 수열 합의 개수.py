def solution(elements):
    answer = set([])
    orig_len = len(elements)
    
    e_copy = elements[:]
    for e in e_copy:
        elements.append(e)
        answer.add(e)
    
    for idx in range(orig_len):
        j = idx 
        total = elements[idx]
        while j < idx + orig_len - 1:
            j += 1
            total += elements[j]
            answer.add(total)
            
        
    return len(answer)