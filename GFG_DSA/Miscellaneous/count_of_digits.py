# GFG Solution
def count_of_digits(x):
    y = 1
    while True:
        x = x//10 # // floor division which removes the last digit
        if x ==0:
            return y
        else:
            y= y+1
print(count_of_digits(9))
