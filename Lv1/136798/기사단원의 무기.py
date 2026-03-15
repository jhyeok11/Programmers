def solution(number, limit, power):
    answer = 0

    for n in range(1, number+1):
        count = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                count += 1
                if i != (n // i):
                    count += 1
                
        if count <= limit:
            answer += count
        else:
            answer += power
        
    return answer

print(solution(5, 3, 2))
print(solution(10, 3, 2))