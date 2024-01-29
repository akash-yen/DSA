# print n times gfg using recursion
def fun(x):
    if x <= 0: # base case where it handels negative numbers as well
        return
    else:
        print('gfg')
    fun(x-1)
# u can always replace a tail recursive to a while loop by 2 steps
# step 1 : replace if with while
# step 2 : change values of parameters at the end of the loop
def tail_while(n):
    while (n!=0):
        print('gfg')
        n=n-1
# factorial of a number
def fac(n):
    if n==0:
        return 1
    else:
        return n * fac(n-1)

# fabonaccii number

def fab(n):
    if n ==0:
        return 0 # todo here I did a mistake I gave 1
    elif n ==1:
        return 1
    else:
        return fab(n-1) + fab(n-2)


# A fun is called tail recursive if the fun does not do anything after the last recursive call even return n*(n-1) is not tail recursive
# advantage of tail recursive is it is optimize by modren compliers
# quick sort and postorder tree traversal are tail recursive

# recursiion practice

def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    print(n)

def log_fun(n):
    if n<=1:
        return 0
    else:
        return 1+fun(n//2)
# the above one gives floor value of log n of base 2

def bin_fun(n):
    if n==0:
        return
    fun(n//2)
    print(n%2)
# the above one gives the binary representation of a given n


def print_n_numbers(n):
    if n <= 0:
        return 0
    else:
        print_n_numbers(n - 1)
        print(n)


def sum_of_digits(x=1):
    if x <= 0:
        return 0
    else:
        return x%10 + sum_of_digits(x//10)
#todo practice this again

def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])





