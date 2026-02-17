def solution(d, budget):
    answer = 0
    sum_d = 0
    
    d.sort()    
    while answer < len(d) and sum_d + d[answer] <= budget:
        sum_d += d[answer]
        answer += 1
        
    return answer

print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))