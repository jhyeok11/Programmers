def solution(arr):
    answer = 0
    sum = 0
    
    for i in range(len(arr)):
        sum += arr[i]
        answer = sum / len(arr)
        
    return answer

print(solution([1,2, 3, 4]))
print(solution([5, 5]))