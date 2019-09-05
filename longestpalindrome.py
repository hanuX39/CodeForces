def longestpalindrome(s,i,j):
    # Recursion
    # if i ==j:
    #     return 1
    # elif s[i]==s[j] and i+1 == j:
    #     return 2
    # elif s[j] == s[i]:
    #     return longestpalindrome(s,i+1,j-1) + 2
    # else:
    #     return max(longestpalindrome(s,i+1,j),longestpalindrome(s,i,j-1))

    # Dp solution
    n = len(s)
    dp = [[0 for i in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    
    for cp in range(2,n+1):
        for i in range(n-cp+1):
            j = i+cp-1
            if s[i] == s[j] and cp == 2:
                dp[i][j] = 2
            elif s[i]==s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]




s = input().strip()
print(longestpalindrome(s,0,len(s)-1))