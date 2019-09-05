# from itertools import permutations

# def check_incr(lst):
#     return lst != sorted(lst)
# def good_bad(A):
#     count = 0
#     A, B =[],[]
#     for i in permutations(A):
#         for a in i:
#             print(a)
#             A.append(a[0])
#             B.append(a[1])
#         print(A,B)
#         print(sorted(A), sorted(B))
#         if check_incr(A) and check_incr(B):
#             count += 1
#     return count

# A = []
# for i in range(int(input())):
#     A.append(input().strip())
# print(good_bad(A))
# for i in A:


# def permutation(lst):  
# 	if len(lst) == 0: 
# 		return []  
# 	if len(lst) == 1: 
# 		return [lst]
# 	l = [] 
# 	for i in range(len(lst)):
#         m = lst[i]
#         remLst = lst[:i] + lst[i+1:]
#         print(remLst)
#         for p in permutation(remLst):
#             print(p)
#             l.append([m] + p) 
# 	return l
def permutation(lst):
    if len(lst)==1:
        return [lst]
    elif len(lst):
        return []
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remlst = lst[:i] + lst[i+1:]
        for p in permutation(remlst):
            l.append([m] + p)
        print(l)
    return l

# Driver program to test above function
i = 0
A = input().strip().split()
A = [char for char in A]
for p in permutation(A):
    print(p)
