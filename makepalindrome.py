def palindrome(str1):
    l,r = 0, len(str1)-1
    k = []
    while(l<r):
        if str1[l] != str1[r]:
            k.append(l)
        l += 1
        r -= 1
    return k
def make_palindrome(str1, queries):
    ans = []
    for i in queries:
        string = str1[i[0]:i[1]+1]
        if len(string) == 1:
            ans.append(True)
            continue
        if i[2] >= len(palindrome(string)):
            ans.append(True)
        else:
            ans.append(False)
    return ans
         
