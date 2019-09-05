from math import log2, floor
def func(a,b,c,n):
    res = a*n
    res += b*n*floor(log2(n))
    res += c*(n**3)
    return res

def solve(a,b,c,k):
    if c != 0:
        mn,mx = 0,floor(k**(1/3))
    else:
        mn,mx = 0,k/max(a,b)    
    ans = 0
    while(mn<=mx):
        mid = (mn + mx)//2
        if func(a,b,c,mid) > k:
            mx = mid-1
        elif func(a,b,c,mid)< k:
            mn = mid + 1
        else:
            ans = mid
            break
    return floor(ans)
a,b,c,k = list(map(int, input().strip().split()))
print(solve(a,b,c,k))
# print(func(2,1,1,23001))