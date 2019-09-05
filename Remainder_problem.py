def remainder(A):
    a,s = [], 0
    for i in A:
        if i[0] == 1:
            a.append((i[1],i[2]))
        else:
            for i in a:
                if i[0]%i[1] == i[2]%i[1]:
                    s += i[1]
            print(s)

for i in range(int(input())):
    if i ==0:
        

