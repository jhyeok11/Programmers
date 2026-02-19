def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum_numbers = numbers[i] + numbers[j]
            if sum_numbers not in answer:
                answer.append(sum_numbers)

    answer.sort()

    return answer

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))