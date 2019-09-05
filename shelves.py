def num_shelves(w, m , n):
    # mi = w
    # if w %s1 ==0:
    #     print(w//s1, 0, 0)
    # elif w%s2 ==0:
    #     print(0, w//s2, 0)
    # else:
    #     for i in range(1,w//s1):
    #         for j in range(1,w//s2):
    #             p = w - (i*s1 + j*s2)
    #             if p >= 0 and mi > p:
    #                 mi = p
    #                 n_s1 = i
    #                 n_s2 = j
    #     print(n_s1, n_s2, mi)
    num_m = 0
    num_n = 0
    rem = w 
    p = 0
    q = 0
    r = 0
    while (w >= n): 
        p = w / m 
        r = w % m 
        if (r <= rem): 
            num_m = p 
            num_n = q 
            rem = r 
        q += 1
        w -= n 
    print( str(int(num_m)) + " " + str(num_n) + " " + str(rem)) 



n, s1, s2 = list(map(int,input().strip().split()))
num_shelves(n, s1, s2)
            
                