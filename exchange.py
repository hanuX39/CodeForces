def currency(n,e,d):
    E = [0,5,10,20,50,100,200]
    D = [0,1,2,5,10,20,50,100]
    mn = 3564864153
    for i in range(len(E)):
        for j in range(len(D)):
            res = n - (e*E[i] + d*D[j])
            if res < mn and res >= 0:
                mn = res
                
    return mn

n = int(input())
d = int(input())
e = int(input())

print(currency(n,e,d))

    

