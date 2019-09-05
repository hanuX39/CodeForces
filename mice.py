def mice(A,B):
    A = sorted(A)
    B = sorted(B)
    print(A, B)
    print(([i-j for i, j in zip(A,B)]))
    return max([abs(i-j) for i, j in zip(A,B)])


A = list(map(int,input().strip().split()))
B = list(map(int,input().strip().split()))
print(mice(A,B))