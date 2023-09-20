#l = [89, 46, 69, 11, 37,57,33,43,23,78,76,445]
# l = [1,2,3,2,3,4,5]
# index = 0
# start = 0
# while start < len(l)-1:
#     l_min = l[start]
#     index = 0
#     for i in l:
#         if i < l_min and i not in l[:start]:
#             l_min = i
#             swap = index
#         index = index+1
#         if l[start] != l_min:
#             l[start],l[swap] = l[swap],l[start]
#     start = start +1
# print(l_min)
# print(l)


l = [4,1,3,2,3,5,4,6,7,5,6,12,33,4]
l_sort = []
start = 0
min = l[start]
while start <= len(l)-1:
    min = l[start]
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
print(l)





