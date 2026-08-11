#getting data(properties and behaviours) from parent clas to child class
#types: 1)single level inheritance  2)multilevel  3)multiple   4)hirarcle   5)hybrid


#EX: parent and child class
# class parent:
#     def __init__(self):
#         self.name="VPro"
# class child(parent):
#     pass
# obj=child()
# print(obj.name)

#ex:
# class parent:
#     def test(self):
#         print("Parent....!")
# class child(parent):
#     def test1(self):
#         print("child")
# class subchild(child):
#     def test2(child):
#         print("subchild")

# obj=subchild()
# obj.test()
# obj.test1()
# obj.test2()


#ex:
# class parent:
#     def test1(self):
#         print("parent")
# class parent1:
#     def test2(self):
#         print("parent1")
# class parent2:
#     def test3(self):
#         print("pareent2")
# class child(parent1,parent2,parent):
#     pass
# obj=child()
# obj.test1()
# obj.test2()
# obj.test3()  
#if 2 classes has same function def,
# whatever the parent classs you called in the obj it will come first

#ex:
# class parent:
#     def __init__(self):
#         self.x=100
# class child1(parent):
#     def __init__(self):
#         super().__init__() #parent level constructor calling to use parent value
#         self.y=200
# class child2(parent):
#     def __init__(self):
#         super().__init__() #parent level constructor calling to use parent value
#         self.y=300
# obj=child1()
# print(obj.x,"....",obj.y)

# obj1=child2()
# print(obj1.x,"....",obj1.y)


# super() is used to call parent class members into child class
# class parent:
#     def __init__(self,par1):
#         self.num1=par1
# class child(parent):
#     def __init__(self,par1,par2):
#         super().__init__(par1)
#         self.num2=par2
# obj=child(200,100)
# print(obj.num1,obj.num2)

#wish() 
# class parent:
#     def test(self):
#         print("parent")
# class child(parent):
#     def wish(self):
#         super().test()
# obj=child()
# obj.wish()    


#Private variables:
# class parent:
#     def __init__(self):
#         self.__x=100  #its a private variable and its only applicable to parent class
# class child(parent):
#     pass
# obj=child()
# print(obj.__x)  #throw error

#Ex:
# class parent:
#     def __test(self):
#         print("hello")
#     def wish(self):
#         self.__test()
# class child(parent):
#     pass
# obj=child()
# obj.wish()

#Ex:Protected variables available only to child class
# _ is used to represent protected variable
#unable to access from other classes

# class parent:
#     def __init__(self):
#         self.x=100
# class child(parent):
#     pass
# obj=child()

#Overiding: means overide parent class function overide with  child class functionality
#overiding comes under polimorphism
# class parent:
#     def db_fun(self):
#         return "mysql"
# class child(parent):
#     def db_fun(self):
#         return "mongodb"
# obj=child()
# print(obj.db_fun())


#ex: Overloading is not supported by python
#same function with multiple parameters called as overloading
# class test:
#     def add(self,num1,num2):
#         res=num+num2
#         print(res)
#     def add(self,num1,num2,num3):
#         res=num1+num2+num3
#         print(res)
# obj=test()

# obj.add(100,200,300)

#
# class test:
#     def add(self,*num):   #num acts like tuple
#         print(sum(num))   #overloading
# obj=test()
# obj.add(10,20)
# obj.add(10,20,30)

#ex:
# class test:
#     college="CBIT !!!"
#     def __init__(self):
#         self.college="KLU  !!!"
# print(test.college)
# obj=test()
# print(obj.college)

#ex:how to modify class level variable
# class test:
#     name="hello"
# test.name="genAI"
# print(test.name)

#ex: Abstarct method : 

# from abc import ABC,abstractmethod
# class test(ABC):
#     @abstractmethod    
#     def my_fun(self):
#         pass
# class test1(test):
#     def my_fun(self):
#         print("Hello")
# obj=test1()
# obj.my_fun()
