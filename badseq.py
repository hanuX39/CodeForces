def badseq(s):
    c,pos = 0,-1
    for i in range(0,n):
        if s[i] == '(': 
            c += 1
        else:
            c -= 1
        if c<0 and pos == -1:
            pos = i
    if c != 0:
        return 'NO'
    if pos == -1:
        return 'YES'
    ss = ''
    for i in range(0,n):
        if i == pos:
            continue
        else:
            ss+= s[i]
    ss += ')'
    w = 0
    for i in range(0,n):
        if ss[i] == ')':
            w -= 1
        else:
            w += 1
        if w<0:
            return 'NO'
    return 'Yes'

n = int(input())
print(badseq(input().strip()))