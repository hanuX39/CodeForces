https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

# Dyanimic programming solution
def lis(arr):
    n = len(arr)
    lis = [1]*n

    for i in range(1,n):
        for j in range(0,i):
            if arr[i]>arr[j] and lis[i]<lis[j]+1:
                lis[i] = lis[j] + 1
                print(arr[i], arr[j], end = '     ')
    maxi = 0
    for i in range(len(lis)):
        maxi = max(maxi, lis[i])

    return maxi

print(lis(list(map(int,input().strip().split()))))
