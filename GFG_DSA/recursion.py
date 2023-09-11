# def fun(x): # stop after 5 runs
#     print('gfg')
#     x = x-1 # base case
#     if x<=0: # <= is a better than ==
#         return
#     fun(x)
# fun(5)

 #def fun():
     #base case

     #recusiive call and approach base cases

#DP, BT, DIvide and conquer(BS,QS,MS)

#tower of Hanoi
#dfs based traversals

# def fac(x):
#     result = x
#     if x == 0 :
#         result = 1
#         return result
#     else:
#         result = result * fac(x-1)
#         return result
#
# print(fac(0))
array = []
# def fib(x):
#     result = 0
#     if x == 0:
#         result = 0
#         return result
#     elif x == 1:
#         result = 1
#         return result
#     else:
#         result = fib(x-1) + fib(x-2)
#         array.append(result)
#         return result

#Tail Recusive optimisization for modren compliations
# exaple quick sort , postorder tree traversal
# merge sort is not tail recusrive so that is one reason quick sort is more efficient
#
# def fun(n):
#     if n==0:
#         return
#     print(n)
#     fun(n-1)
#
# # converting recursiion into iterative by
# # replace if with while
# #change values of parameter at the end of the loop
#
# def fun(n):
#     while(n!=0):
#         print(n)
#         n = n-1
#
# def num(n):
#     if n == 0:
#         return
#     else:
#         num(n-1)
#         print(n)
# num(5)


# def num(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         num(n-1)
#
# num(5)


# def num(n):
#     x = str(n)
#     sum = 0
#     for i in x:
#         sum = sum + int(i)
#     return sum
# print(num(984))


# def getsum(n):
#     sum = 0
#     while n !=0:
#         sum = sum + n%10
#         n = n//10
#     return sum
# print(getsum(120))
#
# sum1 = 0
# def getsumrecu(n):
#     global sum1
#     if n == 0:
#         return 0
#     else:
#         sum1 = sum1 + n%10
#         getsumrecu(n//10)
#     return sum1
# print(getsumrecu(156))

#
# def check(x):
#     z = x[::-1]
#     for i in range(len(z)):
#         if x[i] == z[i]:
#             pass
#         else:
#             return False
#     return True
# print(check('abbcbba'))


