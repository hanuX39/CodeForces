def bit_converter(bit,n):
    if n == len(bit)-1:
        return 2**(len(bit)-1)
    p = (2**(n))*int(bit[n]) + bit_converter(bit, n+1)
    return p
    
def checker(bit):
    i = 0
    num = bit_converter(bit[::-1],0)
    while(True):
        p = 4**(i)
        if p >= num:
            return i
        i += 1

print(checker(input()))