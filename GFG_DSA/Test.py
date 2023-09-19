l = [1,2,3,4,5,6]
def check(l):
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            i=i+1
        else:
            break
    else:
        return l

print (check(l))