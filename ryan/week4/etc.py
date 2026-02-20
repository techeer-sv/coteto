def solution(land):
    dp = land
    for i in range(1, len(land)):
        for j in range(4):
            left = dp[i-1][:j]
            right = dp[i-1][j+1:]
            dp[i][j] += max(left + right)
    return max(dp[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))  # Output: 16