def match(A, str2): # str1 original string str2 the pattern string
    n,i, count = len(str2),0,0
    while(i < len(A)-len(str2)+1):
        p = A[i:len(str2)+i].find(str2) + 1
        if p:
            count += 1
        i += 1
    return count

def string(A,list_str):
    total = 0
    for i in range(len(p)):
        for j in range(i,len(p)):
            str2 = p[i] + p[j]
            if i != j:
                total += match(A,str2)*2
            else:
                total += match(A,str2)

    return total

A = input()
p = []
for _ in range(int(input())):
    p.append(input())
print(string(A,p))
