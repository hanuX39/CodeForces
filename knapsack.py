def maxvalue(W,wt,v,n):
    k = [[0 for _ in range(W+1)] for k in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i==0 or W==0:
                k[i][w] = 0
            elif wt[i-1] <= w:
                k[i][w] = max(v[i-1] + k[i-1][w-wt[i-1]], k[i-1][w])
                # K[i][w] = max(v[i-1] + k[i-1][w-wt[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
    i,j = n,W
    while(i>0 and j>0):    
        if k[i][j] == k[i-1][j]:
            print(i,'--',0, end= ' ')
            i -= 1
        else:
            print(i,'--',1,end =' ')
            i -= 1
            j = j-wt[i] 

    return k[n][w]

# def maxvalue(W,w,v,n):
#     p = sorted([[y,x,y/x] for x,y in zip(v,w)], key = lambda x: x[2], reverse = True)
#     s,k = 0,0
#     for i in range(len(p)):
#         s += p[i][0]
#         k += p[i][1]
#         if s > W:
#             return k-p[i][1]


n = int(input())
W = int(input())
wt = list(map(int, input().strip().split()))
v = list(map(int, input().strip().split()))
print(maxvalue(W,wt,v,n))