def solution(land):
    n = len(land)
    dp = [[0]*4 for _ in range(n)]
    
    for j in range(4):
        dp[0][j]=land[0][j]
        
    for i in range(1, n):
        for j in range(4):
            dp[i][j] = land[i][j] + max(dp[i-1][k] for k in range(4) if k != j) 
            