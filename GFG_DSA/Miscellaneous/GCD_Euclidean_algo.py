def gcd(a,b):
     while a != b:
         if a>b:
             a = a-b
         else:
             b = b-a
     return a

print(gcd(10,5))

# more optimized version 

def gcd_recursion(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

print(gcd_recursion(10,15))