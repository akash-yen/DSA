#prime number

def prime_number_check(n):
    for i in range(2,n):
         if n%i == 0:
            return 'not a prime number'
         else:
            return 'prime'

prime_number_check(10)



import math

def opti_prime_checker(n):
    x = math.sqrt(n)
    x_ = math.ciel(x)
    for i in range(2,x_):
        if n%x == 0:
            return 'Not a prime number'
        else:
            return 'prime number'

opti_prime_checker(36)