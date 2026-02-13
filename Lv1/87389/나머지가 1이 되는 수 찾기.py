def solution(n):
    answer = 0
    arr = []
    
    for i in range(2, n):
        if n%i == 1:
            arr.append(i)
            
    arr.sort()
    answer = arr[0]
            
    return answer

print(solution(10))
print(solution(12))