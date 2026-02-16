def solution(phone_number):
    answer = ''
    lst = list(phone_number)
    length = len(phone_number) - 4
    
    for i in range(length):
        lst[i] = '*'
        
    phone_number = ''.join(map(str, lst))
        
    answer = phone_number
    return answer

print(solution("01033334444"))
print(solution("027778888"))