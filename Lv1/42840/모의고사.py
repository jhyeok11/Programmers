def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_count, b_count, c_count = 0, 0, 0

    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            a_count += 1
        if b[i % len(b)] == answers[i]:
            b_count += 1
        if c[i % len(c)] == answers[i]:
            c_count += 1

    if a_count == max(a_count, b_count, c_count):
        answer.append(1)
    if b_count == max(a_count, b_count, c_count):
        answer.append(2)
    if c_count == max(a_count, b_count, c_count):
        answer.append(3)

    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))