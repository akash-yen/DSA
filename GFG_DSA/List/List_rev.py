# Dynamic Size
# Hetrogenous
# append, insert(1,15), 15 in l , count(30), index(30) careful with index if not there than error, index(30,4,7) start and end index
# remove(data) careful , pop() will retrun as well, pop(2) pop with index, del l[1] index , del l[0:2]
# max(l), min(l), sum(l), l.sort() all need to be in same data type, we can also use x = sorted(l) which will give u a new list where as l.sort() will change the orginal list
# l.reverse()

# list uses array as an undeylying data structure
# in array everything is stored at contigious meamory location i.e each data point is stored at a refreneces
# adv -
# random access i,e we can get the ith item in constant time, set and dict dont have
# cache friendly

#Dis -

#Insertion, Deletion and search are slow
# search is also slow

# Dynamic Size list , pre allocate some extra space

# time complexity of append in list is constant thehta(1) same for pop as well

#insertion is linear

def even_odd_sep(l):
    even = []
    odd = []
    for i in l:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


#################################################################

def get_smaller_in_given_list(l,x):
    res = []
    for i in l:
        if i<x:
            res.append(i)
    return res

############################################

l1 = [10,20,30]
l2 = l1[:]
#print(l1 is l2) # False

##########################################

# list comprehensive is where u can create a another list from an itreable

l1 = [x for x in range(11) if x%2 == 0]

l2 = ["fsdg","asd","gg","datt"]
l3 = [x for x in l2 if x.startswith("g")]
l4 = [x.upper() for x in l2 if x.startswith("g")]

l5 = [1,2,3,4]
d1 = {x:x**3 for x in l5}

d2 = {x: f'ID{x}' for x in range(5)}
d3 = {l2[i] : l5[i] for i in range(len(l2))}

# zip function will do the mapping

d4 = dict(zip(l2,l5))

d5 = {101:'gfg', 103:'practice',102:"ide"}
d6 ={v:k for k,v in d5.items() }


####################################################

def get_max_in_linear_time(l):
    if not l:
        return None   # edge cases
    res = l[0]
    for i in range(1,len(l)):
        if l[i]>res:
            res = l[i]
    return (res)

######################################
l = [] # this is treaded as FALSE
if  l:
    print('a')

#######################################

#TODO REVISION
def sec_max():
    l = [1,34,3,2,19,89,76,45,667,4343,4343,56,2,344,7444,7444]
    max = l[0]
    sec_max = None
    res = 0
    if l == [] or len(l) ==1:
        return None
    else:
        for i in l[1:]:
            if i > max:
                sec_max = max
                max = i
            elif (sec_max == None) or (i > sec_max and i < max):
                 sec_max = i
        return sec_max

####################################################

def is_sorted():
    l = [1,1,2,3,7]
    if len(l) <=1:
        return True
    s_p = l[0]
    for i in l[1:]:
        if s_p > i:
            return False
        else:
            s_p=i
    return True

########################################################

def reverselist(l):
    s=0
    e = len(l)-1
    while s<e:
        l[s],l[e] = l[e],l[s]
        s = s+1
        e = e-1

################################################

l = [10,20,30,40]
temp=l[0]
for i in range(len(l)-1):
    l[i] = l[i+1]
l[len(l)-1] = temp


################################################

l = [10,20,20,20,20,20,30,30,30,40,40,40,50,50,50,50]
s = 1
p = 1
for i in range(1,len(l)):
    if l[i] == l[i-1]:
        s = s + 1
    else:
        l[p] = l[i]
        p=p+1

print(l[:p])

