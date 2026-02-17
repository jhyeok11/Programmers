def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = 0
        sign = 1
        
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 != 0:
            sign = -1
        answer += sign * i
        
    return answer

print(solution(13, 17))
print(solution(24, 27))