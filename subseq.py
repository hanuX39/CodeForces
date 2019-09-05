def subseq(string):
    i,p = 0,[]
    while(i < len(string)):
        if string[i] == '1' and string[i+1] == '0':
            p.append(i)
        i += 1
        if i == len(string)-1 and (string[i] == '1' or string[i] == '0'):
            p.append(i)
            break
    i,r,k = 0,0,[]
    while(i < len(p)):
        l = r
        r = p[i]+1
        sub = string[l:r]
        if len(sub)%2 != 0:
            if '0'*len(sub) != sub:
                k.append('0'*(len(sub)-1) + '1')
            else:
                k.append(sub)
        else:
            if '0'*len(sub) != sub:
                k.append('0'*(len(sub)//2) + '1'*(len(sub)//2))
            else:
                k.append(sub)

        i += 1
    return "".join(k)

p = input()
if len(p)<2000:
    print(subseq(p))
else:
    print('try with some small strings')