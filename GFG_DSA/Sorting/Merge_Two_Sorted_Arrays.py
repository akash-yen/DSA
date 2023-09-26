#merge two sorted list
arr1 = [10,15,20]
arr2 = [5,6,6,30]
# for i in arr1:
#     arr.append(i)
# for j in arr2:
#     arr.append(j)
# for i in range(1,len(arr)): # Here I implemented Insertion sort technique however the thing is like u didnt comsidered the fact that the 2 arrays are sorted
#     for j in range(i):
#         if arr[i] < arr[j]:
#             arr[i],arr[j] = arr[j],arr[i]
# print(arr)


# Merge two sorted arrays

arr2 = [5,10,50,100]
arr1 = [4,30,30,60]
def merge_sort(arr1,arr2):
    arr = []
    sarr1 = 0
    sarr2 = 0
    if arr1[0] < arr2[0]: # we need to have a refrences point since the 2 lists are sorted we can compare the first element
        arr.append(arr1[0])
        sarr1 = sarr1+1
    else:
        arr.append(arr2[0])
        sarr2 = sarr2 + 1
    loop =1
    while loop < len(arr1) + len(arr2):
        if arr2[sarr2] <= arr1[sarr1]:
            arr.append(arr2[sarr2])
            sarr2 = sarr2 + 1
            if sarr2 >= len(arr2): # Once one list is completely inserted to the 3rd list we can append the remianing items
                for i in range(sarr1, len(arr1)):
                    arr.append(arr1[i])
                return arr # this is like an end condition
            loop = loop +1
        else:
            arr.append(arr1[sarr1])
            sarr1 = sarr1 + 1
            if sarr1 >= len(arr1): # Once one list is completely inserted to the 3rd list we can append the remianing items
                for i in range(sarr2, len(arr2)):
                    arr.append(arr2[i])
                return arr
            loop = loop + 1

print(merge_sort(arr1,arr2))


#GFG Solution

def merge(a, b):
    res = []

    m = len(a)
    n = len(b)
    i = j = 0

    while i < m and j < n:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1

    while i < m:
        res.append(a[i])
        i += 1

    while j < n:
        res.append(b[j])
        j += 1

    return res


a = [10, 15]
b = [5, 6, 6, 30, 40]

print(*merge(a, b))

