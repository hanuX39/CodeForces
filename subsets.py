def possible_subsets(A):
    N = len(A)
    sub = 1
    for i in range(1,1<<N):
        p = []
        for j in range(N):
            if (i & (1<<j)):
                p.append(A[j])
        sub = sub*max(p)
    return sub
# print(possible_subsets([2,3]))

# # def setbits(n):
# #     count = 0
# #     while(n):
# #         n = n & (n-1) 
# #         count += 1
# #     return count
# # # 
# # # n = int(input())
# # # for i in range(n):
# #     # print(setbits(int(input())))
# # print(setbits(5))

# def printCombination(arr, n, r): 
#     data = [0]*r
#     combinationUtil(arr, n, r, 0, data, 0)
  
 
# def combinationUtil(arr, n, r, index, data, i):                   
#     if (index == r): 
#         for j in range(r-3): 
#             yield data[j], data[j+1], data[j+2]
#         print() 
#         return
  
    
#     if (i >= n): 
#         return
  
   
#     data[index] = arr[i] 
#     combinationUtil(arr, n, r, index + 1,  
#                     data, i + 1) 
  
    
#     combinationUtil(arr, n, r, index,  
#                     data, i + 1) 
  
# # Driver Code 
# arr = [1, 2, 3, 4, 5]
# r = 4
# n = len(arr)
# print(printCombination(arr, n, r))

g = [(2,3,4),(1,2,5),(9,2,3),(4,3,6)]
g = sorted(g,key=lambda x: x[2])
print(g)