import numpy as np

def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                is_prime = True

                for div in range(2, int(np.sqrt(sum))+1):
                    if sum % div == 0:
                        is_prime = False
                        break

                if is_prime:
                    answer += 1

    return answer

print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))