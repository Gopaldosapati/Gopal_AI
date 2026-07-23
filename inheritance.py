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

#Ex:
