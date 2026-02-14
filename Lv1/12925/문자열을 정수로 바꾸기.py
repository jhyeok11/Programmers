def solution(s):
    answer = 0
    index = 0
    sign = 0
    
    if s[0] == '+':
        index = 1
    elif s[0] == '-':
        index = 1
        sign = -1
    
    for i in range(index, len(s)):
        answer += int(s[i]) * 10**(len(s) - (i+1))
        
    if sign == -1:
        answer *= sign
            
    return answer

print(solution("1234"))
print(solution("-1234"))