def solution(s):
    answer = True
    count_p = 0
    count_y = 0
    
    for i in range(len(s)):
        if s[i] == 'P' or s[i] == 'p':
            count_p += 1
        elif s[i] == 'Y' or s[i] == 'y':
            count_y += 1
            
    if count_p != count_y:
        answer = False

    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))