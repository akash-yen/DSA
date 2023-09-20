l = [89, 46, 69, 1, 37, 80,88,88, 64, 82, 87, 75,75,75]
# selection sort is done via selecting the least element and assigning it postion accordigly
def selection_sort(l):
    start = 0
    while start < len(l)-1: # Running this
        min = l[start] # always compare the min element from the list with its first element
        for i in range(len(l)):
            if i < start:
                pass
            elif l[i] < min:
                index = i
                min = l[i]
            else:
                pass
        if min == l[start]:
            pass
        else:
            l[start],l[index] = l[index],l[start]
        start = start+1
    return l
print(selection_sort(l))