#def merge(arr,l,m,h):

# arr = [10,15,20,11,13]
# l = 0
# h=4
# m=2
# arr = [5,8,12,14,7]
# l = 0
# h=4
# m=3
# x=0
arr = [10,15,20,40,8,11,55]
l = 0
h=6
m=3
x=0
for i in range(m+1,h+1):
    x=x+1
    for j in range(m+1+x): # I can use just high however to optimize I'm using x and I'm adding 1 because
        # i want to check items next to mid as well to be sorted and there is a navie soultion like using 2 sorted arrays merging
        if arr[i] < arr[j]:
            arr[i],arr[j] = arr[j], arr[i]
print(arr)

# GFG Sollution

def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]

    i = j = 0
    k = low

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            a[k] = left[i]

            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1


a = [10, 15, 20, 40, 8, 11, 55]

merge(a, 0, 3, 6)

print(*a)
