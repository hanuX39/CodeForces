def cutroad(n, price):
    # if n <= 0:
    #     return 0
    # mx = 0
    # for i in range(0,n):
    #     mx = max(mx,cutroad(n-i-1, price) + price[i])
    # return mx
    val = [0 for i in range(n+1)]
    val[0] = 0
    for i in range(1,n+1):
        mx = -63265956239
        for j in range(i):
            mx = max(mx,price[j] + val[i-j-1])
        val[i] = mx
    return val[n]

P = list(map(int, input().strip().split()))
print(cutroad(len(P),P))