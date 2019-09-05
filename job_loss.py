def minimisation(V,P):
    V = sorted(V, reverse=True)
    N = len(V)
    result = 0
    for i in range(len(V)):
        result += ((1-P)**(N-i))*V[i]
    return result

V = list(map(int, input().strip().split()))
print(minimisation(V,.1))