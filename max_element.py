def max_min_function(A, start, end):
    mid = (start + end)//2
    if start == mid:
        return min(A[start], A[end]), max(A[start], A[end])
    else:
        start_min, start_max  = max_min_function(A, start, mid)
        end_min, end_max  = max_min_function(A, mid, end)
        return min(start_min,end_min), max(start_max,end_max)

A = [5,84,3,2,35,64,145,224,2448,4848,121848,14894855,578154984,518978,4897,157,85,897,897,981,5798,0,489,548,659,85688,95,598]
n = len(A)
print(max_min_function(A,0,n-2))