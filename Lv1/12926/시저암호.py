def solution(s, n):
    answer = ''
    lst = []
    
    for i in range(len(s)):
        if s[i] == ' ':
            lst.append(' ')
        elif 'A' <= s[i] <= 'Z':
            lst.append(chr((ord(s[i]) - ord('A') + n) % 26 + ord('A')))
        elif 'a' <= s[i] <= 'z':
            lst.append(chr((ord(s[i]) - ord('a') + n) % 26 + ord('a')))
            
    answer = ''.join(lst)
    
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z", 4))