def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    for puddle in puddles:
        x_p = puddle[0]
        y_p = puddle[1]
        dp[y_p][x_p] = -1

    for y in range(1, n+1):
        for x in range(1, m+1):
            if x == 1 and y == 1:
                continue
            if dp[y][x] != -1:
                dp[y][x] = dp[y-1][x] + dp[y][x-1] % 1000000007
            else:
                dp[y][x] = 0
    
    return dp[-1][-1] % 1000000007