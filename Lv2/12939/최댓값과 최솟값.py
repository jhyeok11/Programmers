def solution(s):
    answer = ''

    s = list(map(int, s.split()))
    answer = f"{min(s)} {max(s)}"
    
    return answer

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))