# collection of variables(properties) and functions(behaviour) called as class
# "class" is a keyword used to declre the classes
# "pass" is the key word used to declare empty class
# sharing same copy to multiple objects called as "instance members"
# "self" is the keyword used to declare instance member

# 1)inheritance   2)polymorphism    3)encapsulation    4)abstraction

#ex:
# class test:
#     pass
# obj1=test()  #constructor
# print(obj1)  #hexa decimal value return 
# print(id(obj1))  # convert to decimal

#ex
# class Test:
#     num1=100
# obj1=Test()
# print(obj1.num1)

#ex:
# class Test:
#     num1=100
#     num2=200
# obj1=Test()
# add=obj1.num1+obj1.num2
# print(add)

#ex:
# class Test:
#     def test1(self):   #instance function
#         print("Hello")
#     def test2(self):
#         return "Hello"
#     def test3(self,param1):
#         print(param1)
#     def test4(self,param4):
#         return param4

# obj1=Test()
# obj1.test1()
# res1=obj1.test2()
# print(res1)

# obj1.test3("Hello")

# res2=obj1.test4("Gopal")
# print(res2)


#ex : initialize parameters during obj creation using __init__

# class Test:
#     def __init__(self,x,y):
#         self.num1=x
#         self.num2=y
# obj1=Test(100,200)
# add=obj1.num1+obj1.num2
# print(add)


#ex: 
# class test:
#     def __init__(self,num1):
#         self.num1=num1

#     def test1(self):
#         print(self.num1)
#     def test2(self):
#         return self.num1

# obj1=test(200)
# obj1.test1()
# res=obj1.test2()
# print(res)

#ex:

