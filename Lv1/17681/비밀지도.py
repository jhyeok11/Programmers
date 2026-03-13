def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = format(arr1[i]|arr2[i], 'b').rjust(n, '0')
        result = ''
        for ch in row:
            if ch == '1':
                result += '#'
            else:
                result += ' '
        answer.append(result)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))