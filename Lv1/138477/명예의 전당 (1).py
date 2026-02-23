def solution(k, score):
    answer = []
    hall = []

    for i in score:
        if len(hall) >= k:
            lowest_score = min(hall)
            if lowest_score < i:
                hall.append(i)
                hall.remove(lowest_score)
        else:
            hall.append(i)

        answer.append(min(hall))

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))