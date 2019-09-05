def combinations(A, n):
    sub = []
    N = len(A)
    for i in range(1,1<<N):
        a = []
        for j in range(N):
            if i & 1<<j:
                a.append(A[j])
            if len(a)>=n:
                break
        if len(a)==n:
            sub.append(a)
    return sub
def dietPlanPerformance(calories, k, lower, upper):
    if k == 1:
        combdiet = calories
    else:

        combdiet = self.combinations(calories,k)
    T = 0
    for diet in combdiet:
        smdiet = 0
        if k > 1:
            for i in diet:
                smdiet += i
        else:
            smdiet = diet
        if smdiet < lower:
            T -= 1
        elif smdiet > upper:
            T += 1
    return T
            

print(dietPlanPerformance([1,2,3,4,5],1,3,3))