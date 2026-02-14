def solution(n):
    answer = []
    s = str(n)
    s = s[::-1]
    
    answer = list(map(int, s))
    
    return answer

print(solution(12345))