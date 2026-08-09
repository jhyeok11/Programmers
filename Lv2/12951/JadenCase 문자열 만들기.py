def solution(s):
    answer = ''

    for ch in s.split(' '):
        string = ch.capitalize()
        answer += string + ' '

    return answer[:-1]

print(solution("3people unFollowed me"))
print(solution("for the last week"))