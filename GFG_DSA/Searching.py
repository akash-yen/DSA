# # # sorted array is given we need to find index of a given number
# # array = [10,20,30,40,50]
# #
# # def search(l,n):# n is the number we are searching for
# #     for i in range(len(l)):
# #         if l[i] == n:
# #             return i
# #     return -1
# #
# # print(search(array,20))
#
# ## optimized linear search of a sorted array
# l = [10,20,30,40,50,60,70]
# # def search(l,n): #n is the number we are searching for and l is a sorted array
# #     sta = 0 # start pointer
# #     end = len(l) # end pointer(notice take end pointer as len(l) because if u take as len-1 when u are searching for the last element u will face problem)
# #     mid = ((sta + end) // 2)# carefull when u are using //
# #     while n <= l[len(l)-1]:# this condtion is bcz it is an ordered list so u need to retun -1 if not in the range
# #         mid = ((sta + end )// 2)
# #         if l[mid] == n:
# #             return mid
# #         elif l[mid] > n:
# #             end = mid
# #         else:
# #             sta = mid
# #     return -1
# #
# # # print(search(l,70))
# # l = [10,20,30,40,50,60,70]
#
# #wrong code
# # def rec_ser(l,n,str,end):
# #     str = 0
# #     end = len(l)-1
# #     mid = (str+end)//2
# #     if l[mid] == n:
# #         return mid
# #     else:
# #         if n < l[mid]:
# #             str = 0
# #             end = len(l[:mid])
# #             s=l[str:end]
# #             return rec_ser(l,n,str,end)
# #         else:
# #             str = len(l[:mid])+1
# #             end = len(l)
# #             l = l[str:end]
# #             return rec_ser(l,n,str,end)
# # print(rec_ser(l,30))
#
# def rec_ser(l,n,str,end):
#     if str>end:
#         return -1
#     mid = (str+end)//2
#     if l[mid] == n:
#         return mid
#     elif l[mid] > n:
#         end = mid-1
#         return rec_ser(l,n,str,end)
#     else:
#         str = mid+1
#         return rec_ser(l,n,str,end)
# l = [10,20,30,40,50,60,70]
# print(rec_ser(l,60,str=0,end=len(l)-1))
#
#
#
# # def sqr(n):
# #     for i in range(n):
# #         if i*i == n:
# #             return i
# #         else:
# #             if i*i >n:
# #                 return i-1
# # print(sqr(50))
# #
# def squfloor(n):
#     i=1
#     while i*i <= n:
#         i=i+1
#     return i-1
# l = [1,2,3,4,5,6,7,8,9,10,11]
# def sqr(l,n):
#     s=0
#     e= len(l)-1
#     mid = (s+e)//2
#     while s <=e:
#         mid = (s + e) // 2
#         if l[mid] ==  n :
#             return mid
#         elif l[mid] < n:
#             s = mid+1
#         else:
#             e = mid-1
#     return -1
#
# print(sqr(l,4))
#
# n = 36
# space = list(range(n))
# print(space)
# def sqr(space,n):
#     s=0
#     e= len(space)-1
#     mid = (s+e)//2
#     while s <=e:
#         mid = (s + e) // 2
#         if n//space[mid]*space[mid] == space[mid] :
#             return mid
#         elif space[mid]*space[mid] < n:
#             s = mid+1
#         else:
#             e = mid-1
#     return -1
# print(sqr(space,80))
#
#
#
