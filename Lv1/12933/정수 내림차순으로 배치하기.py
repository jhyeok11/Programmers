def solution(n):
    answer = 0
    a = []
    length = len(str(n))
    
    for i in range(length):
        a.append(n // 10**(length - (i + 1)))
        n = n % 10**(length - (i + 1))
        
    a.sort(reverse = True)
    for i in range(len(a)):
        answer += int(a[i]) * (10**(length - (i + 1)))
    
    return answer

print(solution(118372))