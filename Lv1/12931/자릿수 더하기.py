def solution(n):
    answer = 0
    
    while n >= 10:
        mod = n % 10
        n //= 10
        answer += mod
        
    answer += n

    return answer

print(solution(123))
print(solution(987))