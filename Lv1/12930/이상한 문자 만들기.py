def solution(s):
    answer = ''
    index = 0
    lst = []
    
    for i in s:
        if i == ' ':
            lst.append(' ')
            index = 0
        else:
            if index % 2 == 0:
                lst.append(i.upper())
            else:
                lst.append(i.lower())
            index += 1
            
    answer = ''.join(lst)
                
    return answer

print(solution("try hello world"))