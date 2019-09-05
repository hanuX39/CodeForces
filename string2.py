def fun(A,B):
    for a in A:
        for b in B:
            if a+b not in A and a+b not in B:
                print(a,b)
                break

n = int(input())
A = list(map(int, input().strip().split()))
p = int(input())
B = list(map(int, input().strip().split()))

fun(A,B)
