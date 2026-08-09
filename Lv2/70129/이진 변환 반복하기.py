def solution(s):
    answer = []

    count = 0
    remove_zero_count = 0
    while s != '1':
        remove_zero_count += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        count += 1

    answer = [count, remove_zero_count]

    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))