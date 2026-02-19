def solution(food):
    answer = ''

    for i in range(1, len(food)):
        divisor = food[i] // 2
        answer += str(i) * divisor

    answer = answer + str(0) + answer[::-1]

    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))