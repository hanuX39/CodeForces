def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm

l = [60, 34, 40, 25, 8, 35, 7, 1, 34, 66, 15, 10, 63, 9, 96, 7, 24, 47, 16, 27, 12, 32, 12, 63, 4, 52, 127, 
     8, 11, 43, 18, 30, 35, 56, 127, 19, 44, 24, 12, 40, 8, 4, 43, 24, 8, 31, 19, 78, 48, 29, 96, 25, 40, 1,
     66, 31, 31, 48, 66, 7, 1, 56, 17, 60, 12, 19, 29, 13, 42, 34, 24, 39, 24, 27, 15, 24, 11, 11, 60, 64, 
     24, 15, 12, 48, 63]
lcm = find_lcm(l[0] , l[1])
for i in range(2, len(l)):
	lcm = find_lcm(lcm, l[i])

print(lcm%(10**9+7))


