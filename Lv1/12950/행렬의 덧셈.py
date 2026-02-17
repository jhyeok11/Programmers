def solution(arr1, arr2):
    answer = []
    
    for row1, row2 in zip(arr1, arr2):
        answer.append([i + j for i, j in zip(row1, row2)])
    
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))