# # l = [89, 46, 69, 11, 37,57,33,43,23,78,76,445]
# l = [11,2,3,5,4]
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
#         l[start],l[swap] = l[swap],l[start]
#     start = start +1
# print(swap)
# print(l_min)
# print(l)

l = [1,2,3,7,4,8]
str = 0
min = l[str]
while str < len(l)-1:
    for i in l:
        if i < min:
            min = i
    l[str] = min


