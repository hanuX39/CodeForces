import sys
sys.setrecursionlimit(10**9)

def XOR(a,b,n):
    if n == 0:
        return a
    elif n == 1:
        return b
    return (XOR(a,b,n-1))^(XOR(a,b,n-2))


if __name__ == "__main__":
    a,b,n = list(map(int,input().strip().split()))
    print(XOR(a,b,n))