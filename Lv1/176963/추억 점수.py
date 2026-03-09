def solution(name, yearning, photo):
    answer = []

    for p in photo:
        sum_yearning = 0
        for i, n in enumerate(name):
            if n in p:
                sum_yearning += yearning[i]
        answer.append(sum_yearning)
            
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55],
               [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3],
               [["may"],["kein", "deny", "may"], ["kon", "coni"]]))