#Tuple is a collection of values,heterogeneous ,immutable,ordered,index starts with 0 
# and supports negative indexes
# represent with ()

# a=(10,20,30,40,50)
# print(a)
# print(type(a))
# print(a[1:4])

# a[2]=100
# print(a)

#                    2026-07-20

# a=100,4
# print(type(a))

# a=100,20,30
# print(type(a))
# b=tuple([10,20,30])
# print(type(b))

#Ex: 
# t=(10,20,30)
# list=list(t)  # converting tuple to list
# list[0]=100  # modifying the list values
# t2=tuple(list) # converting list to tuple
# print(t2)
# print(t)  #original tuple not modified

#Ex:
# a=(1,2,3,1,3,2,4,5)
# print(a.count(1))
# print(a.index(3))  #gives first occurance of the element index

#ex:
# a=10,20,30
# e1,e2,e3=a
# print(e1,e2,e3)

# t=10,20,30,40,50
# e1,*e2,e3=t  #e2=[20,30,40]
# a1,*a2=e2    #a2=[30,40]
# x,y=a2
# print(e1,a1,x,y)

#ex: function returning the tuple
# def test():
#     return 10,20,30
# t1=test()
# e1,e2,e3=t1
# print(e1,e2,e3)

#ex:
# t1=((10,20),(30,40),(50,60))
# for inner_list in t1:
#     for index,element in enumerate(inner_list):
#         print(index,element,sep="----->")

