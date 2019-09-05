def tower(n,a,b,c):
    if n == 1:
        print('move disk {} from {} to {}'.format(n,a,b))
        return
    tower(n-1,a,c,b)
    print('move disk {} from {} to {}'.format(n,a,b))
    tower(n-1,c,b,a)
tower(int(input()),'a','c','b')