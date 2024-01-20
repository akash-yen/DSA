def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

def prime_fac(n):
    for i in range(2,n+1):
        if n%i == 0 and is_prime(i):
            if is_prime(i):
                x=i
                while n%x==0:
                    print(i)
                    x = x*i

n = int(input('enter n:'))
prime_fac(n)
