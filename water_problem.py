def solve(A):
    count, a = 0, 0
    result = []
    a_i = [i[0] for i in A]
    b_i = [i[1:] for i in A]
    
    while(len(a_i) != count):
        if b_i[a][0] not in a_i:
            count += 1
            a += 1
            if A[a][1] not in a_i and A[a][0] not in b_i:
                print(a_i[a]+b_i[a])
        if b_i[a][0] in a_i:
            b_i[a] = b_i[a_i.index(b_i[a][0])]
            b_i.pop(a_i.index(b_i[a][0]))
            a_i.pop(a_i.index(b_i[a][0]))
    return count

# n, p = list(map(int,input().strip().split()))
A = [[7, 4, 98], [5, 9, 72], [4, 6, 10], [2, 8, 22], [9, 7, 17], [3, 1, 66]]
# for i in range(p):
#     A.append(list(map(int,input().strip().split())))
print(solve(A))

        


        


