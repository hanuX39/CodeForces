def combinations(A,n):
    sub = []
    N = len(A)
    for i in range(1,1<<N):
        a = []
        for j in range(N):
            if i & 1<<j:
                a.append(A[j])
        if len(a)==n:
            sub.append(a)
    return sub
# import timeit
# import random
# start = timeit.default_timer()
# A = [random.randrange(0,1000) for i in range(100)] 
# print(combinations(A,5))
# stop = timeit.default_timer()
# print(stop-start)


# def swaping(A, B, C):
#     Aa = [a for a in A]
#     N = len(Aa)
#     for i in range(B+1):
#         Aa[i%N], Aa[(i+C)%N] = Aa[(i+C)%N], Aa[i%N]
#     return "".join(Aa)

# print(swaping('raman',1,4))

def transpose(A):
    i,j = 0,len(A)-1
    while(i < j):
            A[i],A[j] = A[j],A[i]
            i += 1
            j -= 1
    print(A)
    i, j = 0,1
    while(i<j and i < len(A)-1):
        print(A[i][j], A[j][i])
        A[i][j], A[j][i] = A[j][i], A[i][j]
        if j == len(A[0])-1:
            i += 1
            j = i+1
            continue
        j += 1
                    
    print(A)

A = [[2,3,5],[6,4,8],[1,7,9]]
print(A)
for i in zip(*A[::-1]):
    print(i)
def HIT(A,X):
    return [a-1 if a > X else a for a in A]
    
n = int(input())
A = list(map(int, input().strip().split()))
for i in range(int(input())):
    p = HIT(A,int(input()))
    A = p
for i in A:
    print(i,end =" ")