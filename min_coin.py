def move(A):
    n = len(A)
    dp = [[0]*n]*n
    mi = 25369858
    # for i in range(n):
    #     for j in range(i+1,n):
    #         dp[i][j] = abs(A[i] - A[j])%2
    #         dp[j][i] = dp[i][j]
    #         print(dp[i][j],'--',abs(A[i] - A[j])%2,end = ' ')
    # print(dp)
    # mi = 36521548786465
    # for d in dp:
    #     if mi > sum(d):
    #         mi = sum(d)
    # return mi
    
    for i in range(n):
        s = 0
        for j in range(n):
            s += abs(abs(A[i] - A[j])%2)
        if mi > s:
            mi = s
    return mi
            

n= int(input())
A = list(map(int,input().strip().split()))
print(move(A))