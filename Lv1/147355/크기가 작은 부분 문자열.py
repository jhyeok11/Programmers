def solution(t, p):
    answer = 0
    length = len(t) - len(p) + 1
    
    for i in range(length):
        if t[i : i+len(p)] <= p:
            answer += 1
            
    return answer

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))