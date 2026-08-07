def solution(board, h, w):
    answer = 0
    dh = [-1, 0, 0, 1]
    dw = [0, -1, 1, 0]

    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if (0 <= h_check < len(board)) and (0 <= w_check < len(board)):
            if board[h][w] == board[h_check][w_check]:
                answer += 1

    return answer

print(solution([["blue", "red", "orange", "red"],
                ["red", "red", "blue", "orange"],
                ["blue", "orange", "red", "red"],
                ["orange", "orange", "red", "blue"]], 1, 1))
print(solution([["yellow", "green", "blue"],
                ["blue", "green", "yellow"],
                ["yellow", "blue", "blue"]], 0, 1))