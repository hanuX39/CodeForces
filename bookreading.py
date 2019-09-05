def number(n,m):
    s,k = 0,[]
    for i in range(1,10+1):
        k.append((i*m)%10)
        s += (i*m)%10
    p = n//(m)
    l = p%10
    return s*(p-l)//10 + sum(k[:l])

for i in range(int(input())):
    n, m = list(map(int,input().strip().split()))
    print(number(n,m))