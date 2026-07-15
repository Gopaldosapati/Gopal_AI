#Loops are used to iterate the collections(lists,tuples)
# a=[10,20,30,40]
# for num in a:
#     #print(num) # iresult will be vertical
#     print(num,end=" ")

#ex-2:
# for a in range(5):
#     print(a)

#ex: 2 include 7 exclude
# for a in range(2,7):
#     print(a)

#ex 2 include ,10 exclude and increment of 2

# for a in range(2,10,2):
#     print(a)

#ex 2 include ,10 exclude and decrease of of -1

# for a in range(2,10,-2):
#     print(a)

# #ex : if i want to print index and value of a list 
# list=[10,20,30,40,50]
# for index,value in enumerate(list):
#     print(index,value,end=" &")


#ex : if i want to print index and value of a list but index starts with 1
# list=[10,20,30,40,50]
# for index,value in enumerate(list,start=1):
#     print(index,value,end=" &")

#ex: iterate 2 lists using zip
# std=["gopal","chetan","aswitha","madhu"]
# marks=[60,70,80,90]
# for std,marks in zip(std,marks):
#     print(std," > " ,marks)

#ex
# a="Hello"
# for ch in (a):
#     print(ch,end=" ")

#ex: reversing the given values

# a="Hello"
# reverse=""
# for ch in a:
#     reverse= ch +reverse
# print(reverse)

#ex : finding the largest number
# a=[10,30,58,20,8]
# largest=a[0]
# for num in a:
#     if num>largest:
#         largest=num
# print(largest)

#ex: count of even numbers in a list
# a=[1,2,3,4,5]
# count=0
# for num in a:
#     if num%2==0:
#         count=count+1
# print(count)

#ex:  print certain range of values from a given range
# for i in range(5):
#     if i==3:
#         break   # used to break the loop
#     print(i)

# else:
#     print("done")

#ex:  continue keyword in for loops
for i in range(5):
    if i==3:
        continue   # used to continue the loop
    print(i)