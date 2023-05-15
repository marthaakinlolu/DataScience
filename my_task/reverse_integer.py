def reverse_integer(x):
    if x < 0:
        sign = -1
        x = abs(x)
    else:
        sign = 1
        
    res = 0
    while x > 0:
        res = res * 10 + x % 10
        x = x // 10
    
    res *= sign
    
    if res < -2**31 or res > 2**31-1:
        return 0
    
    return res
print(reverse_integer(123))