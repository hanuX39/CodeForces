def lbracseq(brac):
    p, count = [],0
    for i in range(len(brac)):
        if brac[i] == '(':
            count += 1
            # p.append(i)
        elif brac[i] == ')':
            count -= 1
            # p.append(i)
        if count ==0:
            mx = i
    return mx -1    
        
print(lbracseq(input().strip()))  