def C(n,r):
    C = [[0 for i in range(r+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,r)+1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][r]



n,m = list(map(int, input().strip().split()))
print(C(n,m))