def all_divsors(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i)
        else:
            pass
#all_divsors(100)

print('-----------------------')
def opt_time_all_divsors(n):
    i = 1
    while i*i <= n:
        if n%i ==0:
            print(i)
            if n/i == i:
                pass
            else:
                print(int(n/i))
        i = i+1


#opt_time_all_divsors(25)


def ordered_opt_time_all_divisors(n):
    i=1
    while i*i < n:
        if n%i == 0:
            print(i)
        i = i+1
    while i>=1:
        if (n%i == 0):
            print(n/i)
        i = i-1
ordered_opt_time_all_divisors(100)