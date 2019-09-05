def paranthesis(i,j,n,S,p):
    # p = []
    # for i in range(len(S)-1):
    #     p.append(chr(65+i))
    # print(p)
    # p.insert(len(p),")")
    # while(j<len(p)):
    #     if S[i+1] == 0:
    #         break
    #     else:
    #         p.insert(S[i],')')
    # p.insert(0,'(')
    # return "".join(p)
    if i==j:
        print(chr(ord(p)+1))
    print("(",end = "")
    paranthesis(i,S[i][j],n,S,p)
    paranthesis(S[i][j]+1,j,n,S,p)
    print(')',end='')


def matmul(arr):
    n = len(arr)
    dp = [[0 for j in range(n)] for i in range(n)]
    S = [[0 for j in range(n)] for i in range(n)]

    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i + L - 1
            p = 1234556987
            for k in range(i,j):
                q = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]
                if q < p:
                    p = q
                    S[i][j] = k
            dp[i][j] = p
    name = 'A'
    paranthesis(1,n-1,n,S,name)


arr = list(map(int, input().strip().split()))
print(matmul(arr))
# print(paranthesis([0,0,1,1,3][::-1]))