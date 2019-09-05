def prime(n):
    i,p = 3,[2]
    while(i<=n):
        t = 0
        for k in p:
            if i%k==0:
                t=1
                break
        if t!=1:
            p.append(i)
        i += 2
    return p, len(p)

print(prime(int(input())))