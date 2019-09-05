def maxsumLIS(a):
    max = 0
    n= len(a)
    maxsum = [a[i] for i in range(n)]
    for i in range(1,n):
        for j in range(i):
            if maxsum[i] < maxsum[j] + a[i] and a[j] < a[i]:
                maxsum[i] = maxsum[j] + a[j]
    for i in range(n): 
        if max < maxsum[i]: 
            max = maxsum[i] 
  
    return max


print(maxsumLIS(list(map(int, input().strip().split()))))