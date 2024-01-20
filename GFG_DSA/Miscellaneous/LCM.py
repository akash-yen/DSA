def lcm(a,b):
    res = max(a,b)
    while True:
        if res%a ==0 and res%b==0:
            return res
        else:
            res = res+1
print(lcm(12,18))


#efficient solution

# a*b = gcd * lcm

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

def lcm_gfg(a,b):
    return a*b/gcd(a,b)

