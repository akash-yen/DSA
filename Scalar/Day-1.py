# question - There is a circular jail with 100 cells numbered from 1 to 100.
# - Each cell has an inmate and the door is initially locked( )
# - One night the jailer gets drunk and he gG"FöühÜiTfe jail in circles.
# In 'ith round' he goes to every door which is multiple of I and changes the state of the
# door. If the door is open, he will close.it and vice versa.
# - He makes a total of 100 rounds, how many prisoners found their door open after 100
# rounds ?

dic = {}
for i in range(1,101):
    dic[i] = 'c'
print(dic)
for i in range(1,101):
    for j in range(1,101):
        if i%j == 0:
            if dic[i] == 'c':
                dic[i] = 'o'
            elif dic[i] == 'o':
                dic[i] = 'c'
print(dic)
z=0
for i in range(1,101):
    if dic[i] == 'o':
        z = z+1
print(z)
# can be done using a list
# filp is one new thing I can lean, c,o can be taken as 1,0
#Time complexty for the above one is n^2 however you can do it in (n+n/2+.....+n/(n-1)+1) - ---> hp == logn  overall nlogn






