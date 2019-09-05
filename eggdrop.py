def egg(n,k):
    # if k ==0 or k == 1:
    #     return k
    # if n == 1:
    #     return k
    # mn = 2369857456
    # for x in range(1, k+1):
    #     res = max(egg(n-1,x-1), egg(n,k-x))
    #     if res < mn:
    #         mn = res
    # return mn + 1 

    dp = [[0 for k in range(k+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][1] = 1
        dp[i][0] = 0
    for i in range(k+1):
        dp[1][i] = i
    for i in range(2,n+1):
        for j in range(2,k+1):
            dp[i][j] = 65456711
            for x in range(j+1):
                res = 1+ max(dp[i-1][x-1], dp[i][j-x])
                if res < dp[i][j]:
                    dp[i][j] = res
    print(dp)
    return dp[n][k] 




print(egg(2,100))