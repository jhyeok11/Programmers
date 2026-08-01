def solution(N, stages):
    fail_rate = {}

    for n in range(1, N + 1):
        reached_player = 0
        not_cleared_player = 0

        for i in range(len(stages)):
            if stages[i] > n:
                reached_player += 1
            elif stages[i] == n:
                reached_player += 1
                not_cleared_player += 1

        if reached_player == 0:
            fail_rate[n] = 0
        else:
            fail_rate[n] = not_cleared_player / reached_player

    answer = sorted(fail_rate, key=lambda x: fail_rate[x], reverse = True)

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
