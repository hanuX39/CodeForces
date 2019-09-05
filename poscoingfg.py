def coin(S,m,n):
    dp = [[0 for _ in range(m)] for k in range(n+1)]
    for i in range(m):
        dp[0][i] = 1
    for i in range(1,n+1):
        for j in range(m):
            x = dp[i-S[j]][j] if i-S[j]>=0 else 0
            y = dp[i][j-1] if j >= 1 else 0

            dp[i][j] = x + y
    print(dp)
    return dp[n][m-1]

print(coin([5,6,2,3],4,20))