def gcd_f(n, m):
    if n >= m:
        if m == 0:
            return n
        else:
            return gcd_f(m, n%m)
    else:
        if n == 0:
            return m
        else:
            return gcd_f(n, m%n)

def solution(n, m):
    answer = []
    gcd = gcd_f(n, m)
    lcm = n * m / gcd
    
    answer.extend([gcd, lcm])
    
    return answer

print(solution(3, 12))
print(solution(2, 5))