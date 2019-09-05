def burger(b,p,f,h,c):
    num_bug = b//2
    if num_bug >= p + f:
        return p*h + f*c
    else:
        if h >= c:
            return h*min(p,num_bug) + f*max(0,num_bug-p)
        else:
            return c*min(num_bug, f) + h*max(0,num_bug-f)

for _ in range(int(input())):
    b, p, f = list(map(int, input().strip().split()))
    h, c = list(map(int, input().strip().split()))
    print(burger(b,p,f,h,c))