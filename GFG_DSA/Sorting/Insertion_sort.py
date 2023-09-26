arr = [20,5,40,60,10,30,30,30,23,666]
#
# def insertion_sort(l):
#     for i in range(1,len(arr)): # the first element is already sorted
#         for j in range(i): # we need to compare only with the sorted array
#             if arr[i] < arr[j]: #need to check only less than is enough as it will take care of > automatically
#                 arr.insert(j,arr[i]) # we are inserting before the greater element so duplicates are also sorted and stabilty is maintained
#                 arr.pop(i+1) # as we are not swapping we need to we need to delete the elemnet
#     return l
#
# print(insertion_sort(arr))


for i in range(1,len(arr)):
    for j in range(i):
        if arr[i] < arr[j]:
            arr[j],arr[i] = arr[i],arr[j] # this will work as you can see that even the swaped element will be compared again and again
        else:
            pass
print(arr)
# For the code wriiten by you the time complexity is always O(n^2) however for the below code if the arr is a sorted arr than O(n) and rever sorted O(n^2)
#GFG CODE

def insertionSort(l):
    for i in range(1,len(l)):
        x = l[i]
        j = i-1
        while j>=0 and x<l[j]:
            l[j+1] = l[j]
            j = j-1
        l[j+1] = x
l = [20, 5, 40, 60, 10, 30]

insertionSort(l)
print(*l)



