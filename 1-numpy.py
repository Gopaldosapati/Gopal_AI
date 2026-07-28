# import numpy as np
# print(np.__version__)

#ex:
# import numpy as abc
# array1=abc.array([10,20,30])   #1D array
# array2=abc.array([[10,20],
#                   [30,40],
#                   [50,60]])     #2D array ---> enclosed with 2 [[ ]]
# arr3=abc.array([[[1,2,3]]])     #3D
# #to check the properties of each array
# print(array1.shape)     # result 3 elements
# print(array1.dtype)
# print(array1.ndim)

#ex:
# import numpy as np
# print(np.zeros((2,3)))      # 2rows and 3 columns with all zeros

# import numpy as np
# print(np.ones((2,3)))          #all 1s

# import numpy as np
# print(np.full((2,3),2))         #all 2s with 2 rows and 3 columns

# import numpy as np
# print(np.eye(3))            #identity matrix

# array4=np.arange(0,10,1)       #derive a 1D array, 0 include 10 exclude and increment of 1
# print(array4)

# array5=np.arange(0,10,2)       #derive a 1D array, 0 include 10 exclude and increment of 2
# print(array5)

# array6=np.linspace(0,1,5) #the difference btween 0 and 1 will be divisible by 5 equal parts  using linear space
# print(array6)

# a=np.full(5,3)
# print(a)

# b=np.full((2,3),5)
# print(b)


#ex: accessing elements
import numpy as np
# a=np.array([1,2,3,4,5])
# print(a[0],a[-5])
# print(a[0:3]) # 0 include 3 exclude
# print(a[:2])  # 2 exclude
# print(a[2:])  # from position 2 it will return  all
# print(a[::-1]) # reversing the list
# print(a[::-2])
# print(a[::2])
# print(a[::3])

# a=np.array([[10,20],
#             [30,40]])
# print(a[0][0],a[0][1],a[1][0],a[1][1])

#ex:
import numpy as np
# a=np.array([1,2,3,4,5])
# for element in a:
#     print(element,end=" | ")
#     print()
    
# for index,element in enumerate(a):     # to get index and value from array
#     print(index,element,sep="-->")

#ex:
# a=np.array([[10,20,30],[40,50,60]])
# for inner_list in a:
#     for index,element in enumerate(inner_list):
#         print(index,element,sep="---->")
#     print("-------------------------------------")

#ex:
# import numpy as np
# a=np.array([1,2])
# b=np.array([3,4])
# c=a+b
# print(c)
# d=a-b
# print(d)
# e=a*b
# print(e)


#------------------------2026-07-28----------------------

#ex:
# import numpy as np
# a=np.array([10,20,30])
# num=2
# print(a+num)  #add +2 to each element in the array 

# b=np.array([[10,20,30],
#             [40,50,60]])
# x=10
# print(b+x)

#ex: convert 1D array to 2D array
# import numpy as np
# a=np.array([1,2,3,4,5,6])
# print(a.reshape(2,3))
# b=a.reshape(2,3)  # flatten used to convert to 1D
# print(b.flatten())

#ex: inverse function

# import numpy as np
# a=np.array([[10,20],
#             [30,40]])
# print(np.linalg.inv(a))  #matrix inverse
# print(np.linalg.det(a))   #determinent
# print(np.linalg.matrix_transpose(a))


#ex:
# import numpy as np
# a=np.array([60,68,80,78,69,90])
# print(f"avg marks : {np.mean(a)}")
# print(f"avg marks : {np.max(a)}")

#Ex:
# import numpy as np
# sales=np.array([[200,300,250],
#                 [400,500,450]])
# print(np.sum(sales,axis=1))  #row wise cal
# print(np.sum(sales,axis=0)) #column wise cal


#ex:

