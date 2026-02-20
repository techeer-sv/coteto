def solution(arr1, arr2):
    x = len(arr1)
    y = len(arr2[0])
    yy = len(arr2)
    answer = [[0] * y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            for k in range(yy):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])) # [[4, 7], [6, 5], [7, 4]]