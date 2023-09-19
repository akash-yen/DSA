# l = [2,3,4,5,6,1,2,1]
# l.sort() # will modify the original list
# print(l)
#
# tup = (2,3,4,51,12,2,32,)
# new = sorted(tup)
# print(tup)
# print(new)

# def sort_criteria(l): # here we are sorting according to our foumulae
#     return len(l)
# l = ['Akash','Ram','Pavan']
#
# l.sort(key=sort_criteria)
# print(l)
#
# l2 = ['SS','Ram','Pavan','Akash']
#
# l2.sort(key=sort_criteria,reverse=True)
# print(l2) # here len of akash and pavan are same however the one which comes first in the l2 the same order is preserved

#
# class Point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# def my_fun(p):
#     return p.x
#
# l = [Point(1,2),Point(3,4),Point(5,6)]
# l.sort(key=my_fun)
# check = Point(1,2).x
# print(check)

#Bubble sort


l = [89, 46, 69, 1, 37, 80,88,88, 64, 82, 87, 75]

# def bubble_sort(l):
#     rounds = len(l) -1 # to run the while loop n-1 times
#     optimizer = 1 # making less runs than ususal
#     while rounds !=0 :
#         for i in range(len(l)-optimizer):
#             if l[i] > l[i+1]:
#                 l[i],l[i+1] =  l[i+1], l[i] #swaping the postions
#             else:
#                 pass
#         rounds = rounds -1
#         optimizer = optimizer +1
#     return l
# print(bubble_sort(l))

# def bubble_sort(l):
#     rounds = len(l) -1 # to run the while loop n-1 times
#     optimizer = 1 # making less runs than ususal
#     while rounds !=0 :
#         for i in range(len(l)-optimizer):
#             if l[i] > l[i+1]:
#                 l[i],l[i+1] =  l[i+1], l[i] #swaping the postions
#             else:
#                 pass
#         rounds = rounds -1
#         optimizer = optimizer +1
#     return l
# print(bubble_sort(l))

# optimized code if given a sorted array
l = [1,2,3,4,5,6]
def bubble_sort(l):
    rounds = len(l) -1 # to run the while loop n-1 times
    optimizer = 1 # making less runs than ususal
    def check(l): # I defined another fucntion to check whether the given list is already a sorted list or not if soreted no need to run loops
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                i = i + 1
            else:
                break
        else:
            return l
    if check(l) == l:
        return l
    else:
        while rounds !=0 :
            for i in range(len(l)-optimizer):
                if l[i] > l[i+1]:
                    l[i],l[i+1] =  l[i+1], l[i] #swaping the postions
                else:
                    pass
            rounds = rounds -1
            optimizer = optimizer +1
        return l
print(bubble_sort(l))


