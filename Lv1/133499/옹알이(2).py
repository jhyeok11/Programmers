def solution(babbling):
    answer = 0
    babble = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        word = babbling[i]
        prev = ''
        while word:
            matched = False
            for j in range(len(babble)):
                if prev == babble[j]:
                    continue

                if word.startswith(babble[j]):
                    matched = True
                    word = word[len(babble[j]):]
                    prev = babble[j]
                    break

            if not matched:
                break

        if not word:
            answer += 1
            
    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))