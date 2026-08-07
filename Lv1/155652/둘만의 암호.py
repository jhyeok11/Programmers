def solution(s, skip, index):
    answer = ''

    for ch in s:
        count = 0
        while count < index:
            ch = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
            if ch not in skip:
                count += 1
        answer += ch

    return answer

print(solution("aukks", "wbqd", 5))