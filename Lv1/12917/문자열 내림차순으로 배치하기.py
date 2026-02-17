def solution(s):
    answer = ''
    
    lst = list(s)
    lst.sort(reverse = True)
        
    answer = ''.join(map(str, lst))
    
    return answer

print(solution("Zbcdefg"))