def solution(wallet, bill):
    answer = 0

    while (max(wallet) < max(bill)) or (min(wallet) < min(bill)):
        bill[bill.index(max(bill))] //= 2
        answer += 1

    return answer

print(solution([30, 15], [26, 17]))
print(solution([50, 50], [100, 241]))