def solution(n):
    answer = 0
    ternary = []
    
    while n > 0:
        mod = n % 3
        n //= 3
        ternary.append(mod)

    for i in range(len(ternary)):
        answer += 3**(len(ternary) - (i + 1)) * ternary[i]
        
    return answer

print(solution(45))
print(solution(125))