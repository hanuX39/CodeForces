def coin(S,m,n):
    table = [0]*(n+1)
    table[0] = 1
    for i in range(m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
    print(table)
    return table[n]


S = list(map(int, input().strip().split()))
m = len(S)
n = int(input())
print(coin(S,m,n))