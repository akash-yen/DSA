def isPal(num):
    empty_list = []
    while num > 0:
        empty_list.append(num % 10)
        num = num // 10
    if empty_list == empty_list[::-1]:
        return True
    else:
        return False
print(isPal(10101))


from count_of_digits import count_of_digits
def isPal_gfg(n):
    z =n
    x = 0
    temp=0
    while n > 0:
        x = n%10
        y = count_of_digits(n)
        temp = temp+(x*10**(y-1))
        n = n//10
    if temp == z:
        return True
    else:
        return False
print(isPal_gfg(12321))


# The most effiecent one

def isPal_eff(n):
    rev = 0
    temp = n
    while temp != 0:
        ld = temp%10
        rev = rev*10 + ld
        temp = temp//10
    return rev == n # this is a consise code 
print(isPal_eff(101))