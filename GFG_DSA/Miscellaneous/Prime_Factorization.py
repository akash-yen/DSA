def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

def prime_fac(n):
    for i in range(2,n+1):
        if n%i == 0 and is_prime(i):
            x = i
            ifls
