def com_div(A):
    p = min(A)
    count = 0
    for i in range(2,p+1):
        s = sum([a%i for a in A])
        if s == 0:
            count += 1
    return count + 1

n = int(input())
A = list(map(int, input().strip().split()))
print(com_div(A))