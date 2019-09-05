def bad(S):
    mn = 254894514
    count = 0
    for i in range(len(S)-1,-1,-1):
        if S[i] > mn:
            count += 1
        mn = min(mn, S[i])
        
    return count


for i in range(int(input())):
    n = int(input())
    S = list(map(int, input().strip().split()))
    print(bad(S))