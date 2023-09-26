l = [89, 46, 69, 1, 37, 80,88,88, 64, 82, 87, 75,75,75]
# selection sort is done via selecting the least element and assigning it postion accordigly
def selection_sort(l):
    start = 0
    while start < len(l)-1: # Running this to move the star pointer to the right side
        min = l[start] # always compare the min element from the list with its first element after every while loop
        for i in range(len(l)): # to find the min element from the remianing sub-array
            if i < start:
                pass
            elif l[i] < min:
                index = i
                min = l[i]
            else:
                pass
        if min == l[start]: # no swap if duplicates are present as stabilty is not maintained
            pass
        else:
            l[start],l[index] = l[index],l[start] # here the swap happens
        start = start+1
    return l
print(selection_sort(l))

# GFG SOLUTION
def selectSort(l):
    n = len(l)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if l[j] < l[min_ind]:
                min_ind = j
        l[min_ind], l[i] = l[i], l[min_ind]


l = [10, 5, 8, 20, 2, 18]

selectSort(l)

print(*l)

