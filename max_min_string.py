def max_min_string(n,l,r):
    mi, mx = 0,0
    k = [2**i for i in range(n)]
    print(k)
    for i in range(l):
        if i == 0:
            mi = mi + k[i]*(n-l+1)
        else:
            mi += k[i]
    for i in range(l):
        if i == 0:
            mx += k[n-i-1]*(n-l+1)
        else:
            mx += k[n-i-1]
    return mi, mx

n,l,r = list(map(int, input().strip().split()))
print(max_min_string(n,l,r))

