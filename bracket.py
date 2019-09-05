def balanced(s):
    # print(s)
    if len(s)%2 != 0:
        return "NO"
    s = [char for char in s]
    pos = [i for i in range(len(s)) if s[i]=='(']
    # print(pos)
    p, count, sm, i = 0, 0, 0, 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
            p += 1
            # print(s[i],'---',count)
        elif s[i] == ')':
            count -= 1
            # print(s[i],'---',count)
        if count < 0:
            sm += pos[p] - i
            s[i], s[pos[p]] = s[pos[p]], s[i]
            p += 1
            count = 1
            # print(s)
        if sm > 1:
            return 'NO'
    # print("".join(s))
    return 'YES'

n = int(input())
print(balanced(input().strip()))

