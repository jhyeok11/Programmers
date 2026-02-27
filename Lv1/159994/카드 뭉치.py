def solution(cards1, cards2, goal):
    answer = 'Yes'
    n, m = 0, 0

    for i in range(len(goal)):
        if (n < len(cards1)) and (goal[i] == cards1[n]):
            n += 1
        elif (m < len(cards2)) and (goal[i] == cards2[m]):
            m += 1
        else:
            answer = 'No'

    return answer

print(solution(["i", "drink", "water"], ["want", "to"],
               ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"],
               ["i", "want", "to", "drink", "water"]))