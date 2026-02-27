def solution(land):
    n = len(land)
    dp = [[0]*4 for _ in range(n)]

    for j in range(4):
        dp[0][j] = land[0][j]

    for i in range(1, n):
        for j in range(4):
            best = 0
            for k in range(4):
                if k == j:
                    continue
                if dp[i-1][k] > best:
                    best = dp[i-1][k]
            dp[i][j] = land[i][j] + best

    return max(dp[n-1])