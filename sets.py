# # set never allows duplicates ,unordered, hetergeneous and no indexes,searchable. 

# # Hashable.represented as set() or {}

# s1={10,20,30,10,20,30}
# print(s1)-- removed duplicates

# s1=set((10,20,30,10))
# print(s1)

# s1=set([10,20,10,30])
# print(s1)

# s5=set()
# s6={}
# print(type(s5)) ---empty set
# print(type(s6)) ---empty dict


#ex:
# s1={10,20,10,20,30}
# print(s1)

# s2=set([10,20,10,20,30])
# print(s2)

# s3={}
# print(type(s3))

# s4=set()
# print(type(s4))

# s5=set({30,20,10})
# print(s5)

############################22-07-2026#####################
#ex:
# s1={10,20}
# s1.add(30)
# s1.update([40,50])   #if we add more elements we need to use update function
# s1.remove(10)   #to delete a particular element
# print(s1)  # unorderd
# print(s1.pop())
# print(s1)
# s1.clear()  #to clear all the elements
# print(s1)


#ex: check the element present or not
# s1={10,20,30}
# print(20 in s1)
# print(40 in s1)
# print(200 in s1)

#ex:
# s1={1,2,3}
# s2={3,4,5}
# print(s1.union(s2))  #it will remove duplicate in both and give uniq
# print(s1 | s2)       #it will remove duplicate in both and give uniq
# print(s1.intersection(s2)) #it will common element in both sets
# print(s1 & s2) #it will common element in both sets
# print(s1 - s2)   # remove the common element and return other elements from s1
# print(s1 ^ s2)   # remove common element fromboth sets and return other elements

#ex:
