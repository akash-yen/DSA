def is_prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
def all_prime(n):
    for i in range(2,n+1):
        if is_prime(i) == True:
            print(i)
#all_prime(23)


######################################

# Optimization

def sieve(n):
    if n<=1:
        return

    isPrime = [True]*(n+1)

    i = 2
    while i*i <= n:
        if isPrime[i]:
            for j in range(2*i, n+1,i):
                isPrime[j] = False
        i = i+1
    for i in range(2,n+1):
        if isPrime[i]:
            print(i,end=" ")

sieve(100)