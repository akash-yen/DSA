l = [89, 46, 69, 11, 37, 80,88,88, 64, 82, 87, 75]
l_min = l[0]
index = 0
for i in range(len(l)-1):
    if l[i] < l_min:
        l_min = l[i]
        index = i
print(l_min,index)