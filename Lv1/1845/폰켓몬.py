def solution(nums):
    answer = 0
    arr = []
    
    for i in nums:
        if i not in arr:
            arr.append(i)

    if len(arr) <= len(nums)/2:
        answer = len(arr)
    else:
        answer = len(nums) // 2

    return answer

print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))