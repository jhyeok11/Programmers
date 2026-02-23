def solution(a, b, n):
    answer = 0

    while n >= a:
        divisor = n // a
        mod = n % a
        n = b * divisor + mod
        answer += b * divisor

    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))