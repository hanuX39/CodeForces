import sys
# data = []
# for k in range(10):
#     a = len(data)
#     b = sys.getsizeof(data)
#     print('length : {} and size of data is {}, with list is {}'.format(a,b, data))
#     data.append(chr(65 + k))

import random
for i in range(10):
    print(random.randrange(0,100))

# def tostring(list):
#     return "".join(list)
# def permutation(A, l, r):
#     if l == r:
#         print tostring(A)
#     else:
#         for i in range(l,r+1):
#             A[l], A[i] = A[i], A[l]
#             permutation(A,l+1,r)
#             A[l], A[i] = A[i], A[l]

# permutation[['A','B','C','D'],0,3]
# import numpy as np
# i = np.array([5,4,2,3,6])
# k = np.sort(i)[:3]
# print(k)
# print(np.partition(i,3)[:3])
# print(np.argpartition(i,3)[:3])
# fahrenheit = 54
# print(f'The temperature is {fahrenheit} degrees F ({int((fahrenheit - 32) * (5.0/9.0))} degrees C).')
# print('The temperature is {} degrees F ({} degrees C).'.format(fahrenheit, int((fahrenheit - 32) * (5.0/9.0))))

