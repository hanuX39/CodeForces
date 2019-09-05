A = []
for i in range(int(input())):
    a,x,y = list(map(int, input().strip().split()))
    s = 0
    if a == 1:
        A.append((x,y))
    elif a == 2:
        for i in A:
            if i[0]%x == y%x:
                s += i[1]
        print(s)

