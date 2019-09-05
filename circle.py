def number(A):
    s = 0
    for i in A:
        s = 10*s + i
    return s
def check(A):
    p = [i for i in range(1,max(A)+1)]
    if len(A) <= 3:
        return 'YES'
    i = 0
    while(True):
        q = A.pop(-1)
        A.insert(0,q)
        if number(A) == number(p) or number(A[::-1]) == number(p):
            return 'YES'
        elif i == len(A):
            return 'NO'
        i += 1

for _ in range(int(input())):
    n =  int(input())
    A = list(map(int, input().strip().split()))
    print(check(A))
