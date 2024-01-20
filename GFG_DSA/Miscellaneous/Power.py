def power(a,b):
    res = 1
    for i in range(1,b+1):
        res = res*a
    return res

print(power(2,3))


# optimization

def power_rec(a,n):
    if n==0:
        return 1
    temp = power(a,n//2)
    temp = temp * temp
    if (n%2 ==0):
        return temp
    else:
        return temp *a

