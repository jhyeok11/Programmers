def solution(s):
    answer = ''
    divisor = len(s) // 2
    
    if len(s) % 2 == 0:
        answer = s[divisor-1] + s[divisor]
    else:
        answer = s[divisor]
        
    return answer

print(solution("abcde"))
print(solution("qwer"))