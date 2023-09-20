# l = [10,41,30,15,80]
# def sort_o_e(l):
#     o=[]
#     e=[]
#     for i in l:
#         if i%2 ==0:
#             e.append(i)
#         else:
#             o.append(i)
#     return o,e
# even, odd =sort_o_e(l)
# print(even)
# print(odd)
#
# l = [i*i for i in range(10) if i<5]
# print(l)
# x = 'asd'
# x.startswith('a')
# print(x)

# d = {x:f'id{x}' for x in range(10)}
# print(d)
#
# l1 = [1,2,3,4]
# l2 = [9,8,7,6]
# d3 = dict(zip(l1,l2))
# print(d3)

# l = [60]
#
# max = 0
# for i in l:
#     if i > max:
#         max = i
# print(max)


# l = [10,10,10]
# max = 0
# for i in l:
#     if i > max:
#         max = i
# print(max)
# sec_max = 0
# for i in l:
#     if i < max and i> sec_max:
#         sec_max = i
# print(sec_max)
#
# l = [15,12,20,15]
# max = 0
# smax = 0
# for i in l:
#     if i > max:
#         max = i
#     elif i>smax and  max>smax and i!=max:
#         smax = i
# print(max,smax)
#
# l = [10,20,30,40]
# def getsecmax(l):
#     if len(l) <=1:
#         return None
#     lar = l[0]
#     slar = None
#     for x in l:
#         if x > lar:
#             slar = lar
#             lar = x
#         elif x!= lar:
#             if slar == None or slar < x:
#                 slar = x
#     return slar
# print(getsecmax(l))

# l = [10,5,30]
# def check_sort(l):
#     if l == [] or len(l) ==1:
#         return 'yes'
#     b = None
#     a = None
#     for i in range(len(l)):
#         if i ==0 and l[i+1] > l[i]:
#             pass
#         elif i == (len(l)-1) and l[i] >= l[i-1]:
#             pass
#         elif l[i] <= l[i+1] and l[i] >= l[i-1]:
#             pass
#         else:
#             return 'No'
#     return 'Yes'
# print(check_sort(l))

# l = [10,20,40,20]
# def check(l):
#     if l == [] or len(l) ==1:
#         return 'Yes'
#     else:
#         i=1
#         while i<len(l)-1:
#             if l[i] <= l[i+1]:
#                 i=i+1
#             else:
#                 return 'No'
#     return True
# print(check(l))


# l = [10,20,30]
#
# def back(l):
#     l2 = []
#     i=0
#     while i<len(l):
#         l2.append(l[len(l)-i-1])
#         i=i+1
#     return l2
# print(back(l))

# def rev(l):
#     s=0
#     e = len(l)-1
#     while s<e:
#         l[s],l[e]=l[e],l[s]
#         s=s+1
#         e=e-1
#     return l
# l=[10,30,40]
# print(rev(l))

# l = [1,2,3,4]
# def lrotate(l):
#     rotate = [l[0]]
#     new = l[1:] + rotate
#     return new
# print(lrotate(l))

# l = [1,2,3,4]
# s=0
# e = l[0]
# for i in range(len(l)-1):
#     l[i] = l[i+1]
# l[len(l)-1] = e
# print(l)

l = [1,1,2,2,3,4,4,4,5,5,5,5,5,6]

# def dup(l):
#     f=1
#     for i in range(1,len(l)):
#         if l[f-1] != l[i]:
#             l[f] = l[i]
#             f=f+1
#     return  f,l
# print(dup(l))

