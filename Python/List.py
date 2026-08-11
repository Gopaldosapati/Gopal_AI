#list is a collection of values,heterogenious and ordered- index starts with 0 
#allow duplicates
# represent with []
# list is a mutable object and we can modify the objects with in list

# num=["VPro",10,10.2,True]
# print(type(num))
# print(num[1])

# a=[10,20,30,40,40]
# print(a)
# print(a[2])       #30
# print(a[-3],a[2])  #30,30

# a=[10,20,30,40,40]
# print(a[0:3])   # index 0 included and index 3 excluded. ans :[10,20,30]
# print(a[:3])    # index 3 excluded  [10,20,30]

# we can perform sum,min,max,sort,length operations on the list

# a=[10,20,30,40,50]
# a[0]=100
# print(a)

# -------------------------------------17/07/2026------------------------------
# a=[10,20,30]
# print(a)

# b=list((11,2,3,4))
# print(b)

# c=list("Hello")  #string converted to char array
# print(c)

#ex:
# a=[10,20,30,40]
# print(a[1],a[3])
# print(a[1:3])

# rev=a[::-1]
# print(rev)

# res1=a[::-2]
# print(res1)   #it will eturn every 2nd element in the list

# res2=a[::-3]
# print(res2)    #it will eturn every 3nd element in the list

#ex: append and extend
# a=[10,20,30]
# a.append(40)
# print(a)
# b=[50,60]
# a.extend (b)  # list b added to list a as extend
# print(a)

# a.insert(1,15)
# print(a)  #insert 15 at index 1

# a.remove(10)
# print(a)  #it will remove first occurance of 10 from list

# a.pop()
# print(a)   #it will remove last element

# a.sort()
# print(a)  #ascending order

# a.sort(reverse=True)
# print(a)  #descending order


#ex  shallow copy

# a=[10,20,30]
# b=a #if i modify one list other list also got modified because both are sharing same location/address
# print(a)
# b.append(50)
# print(b)
# print(a)

#ex:
# a=[[10,20],[30,40,50]]
# b=a
# a[0][0]=100
# print(a)
# print(b)

#ex deepcopy
# import copy
# a=[[10,20],[30,40,50]]
# b=copy.deepcopy(a) # copy the elements of a. If a modify b wont.
# a[0][0]=100
# print(a)
# print(b)   # elements wont change

# #ex:
# a=[1,2,3,4,5,6,7,1,1]
# print(len(a))
# print(max(a))
# print(sum(a))
# print(sum(a)/len(a))
# print(a.count(1))
# b=sorted(a)  # sorted elements will be added to b
# print(b)
# print(a)


#Ex: removing duplicatees using fromkeys in a list
# a=[1,2,2,3,3,4,5,6,6,7]
# uniq_a=list(dict.fromkeys(a))
# print(uniq_a)

#ex: 2d and 3d list creation
# a=[[]]
# print(a*3)
# b=a*3
# print(b)

#ex:get the memory loction of a index
# a=[10,20,30]
# print(id(a))
# a.append(40)   #append will not change the memory location
# print(id(a))

#ex:
# a=[10,20,30]
# print(id(a))
# b=a+[40]   # will change the memory location
# print(id(b))

#ex: get the even cube results and sum the result using map,reduce and filter finctions
# from functools import reduce
# a=[1,2,3,4,5]
# cubes=map(lambda x:x*x*x,a) #
# even=filter(lambda b:b%2==0,cubes)
# res=reduce(lambda num1,num2:num1+num2,even)
# print(res)

#ex: remove false values
# a=[0,1,False,3,4]
# res=list(filter(None,a))  #None is used to remove false values like 0,False,''
# print(res)

# a=[0,1,False,3,4]
# res=list(filter(None,a))  #None is used to remove false values like 0,False,''
# print(res)

#ex:
# a=[1,2,3,4,5]
# print([i for i in a if i%2==0])

#ex:
# a=[1,2,3]
# a.append([4,5])
# print(a)

# a=[1,2,3]
# a.extend([4,5]) # extend used to add 4,5 to the list a
# print(a)

