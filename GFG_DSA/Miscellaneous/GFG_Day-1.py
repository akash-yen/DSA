#sum of n natural numbers
#way -1
n = int(input('enter the num for n natural sum'))
sum=0
for i in range(1,n+1):
    sum = sum+ i
print(sum)
#order of growth is constant c1
#way-2

n = int(input('enter the num for n natural sum'))
sum = n*(n+1)/2
print(sum)
#order of growth is c2n + c3

#way-3 using 2 loops
n = int(input('enter the num for n natural sum'))
sum=0
for i in range(1,n+1):
    for j in range(i):
        sum = sum+1
print(sum)
#order of growth is c4n*n + c5n + c6




