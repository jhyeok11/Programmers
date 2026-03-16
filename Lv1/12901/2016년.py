def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31,30, 31, 31,30, 31, 30, 31]
    sum_days = 0

    sum_days = sum(month[:a-1]) + b
    
    if sum_days % 7 == 1:
        answer = 'FRI'
    elif sum_days % 7 == 2:
        answer = 'SAT'
    elif sum_days % 7 == 3:
        answer = 'SUN'
    elif sum_days % 7 == 4:
        answer = 'MON'
    elif sum_days % 7 == 5:
        answer = 'TUE'
    elif sum_days % 7 == 6:
        answer = 'WED'
    else:
        answer = 'THU'

    return answer

print(solution(5, 24))