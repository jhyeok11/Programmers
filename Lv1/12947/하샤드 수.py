def solution(x):
    answer = True
    s = str(x)
    sum = 0
    
    for i in range(len(s)):
        sum += int(s[i])
        
    if x % sum != 0:
        answer = False
        
    return answer

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))