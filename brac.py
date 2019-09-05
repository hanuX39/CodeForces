def sequ(A):
    if max(A) == A[(len(A))/2] or max(A) == A[len(A)/2 -1]:
        return True
    return False
def balanced(str1):    
    A, count = [], 0
    for i in range(len(str1)):
        if str1[i] == "(":
            if i == 0:
                A.append(1)
            else:
                A.append(1 + A[i-1])
        elif str1[i] == ")":
            A.append(-1+A[i-1])
    print(A)
    assert len(A) == len(str1)   
    p = []
    for i in range(len(A)):
        if A[i] == 1 and i == 0:
            p.append(i)
        elif A[i-1] == 0 and A[i] == 1:
            p.append(i)
        elif A[i] == 0:
            p.append(i)
    l = []
    print(p)
    for i in range(0,len(p),2):
        k = A[p[i]:p[i+1]+1]
        if max(A) == k[(len(k))//2] or max(k) == k[len(k)//2 -1]:
            l.append(p[i+1]-p[i]+1)
    return max(l)


print(balanced(input().strip()))