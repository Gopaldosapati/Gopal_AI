# # is a particular business task or set of statements also called a function
# # we can reuse a function
# # "def" is a keyword used to create a fuction
# # "pass" is the keyword , used to declare an empty function

# # ex1: no params and no return type
# def addition():
#     num1=200
#     num2=100
#     res=num1+num2
#     print(f"addition of 2 numbers:{res}")

# addition()

# # ex:2 no params with return type

# def addition():
#     num1=200
#     num2=300
#     res=num1+num2
#     return res
# x=addition()
# print(f"result is:{x}")

# #ex:3  with params but no return type
# def addition(a,b):
#     res=a+b
#     print(f"addition is :{res}")
# addition(100,200)


# ex-4 with params and return type
# def addition(a,b):
#     res=a+b
#     return res

# x=addition(200,300)
# print(f"addition is:{x}")


# ex:5 default params. while declaring func initializing values

# def test(name="VPro"):
#     print(name)
# test()

# ex:6

# def test(a=100,b=200):
#     print(a,b)
# test()
# # test(300,400)--override with these values
# test(b=500)

# ex:7 normal and default params. Default params should me at the end of the function
# def test(a,b=100):
#     print(a,b)

# test(100,200)
# test(1000)

# ex:8 square cal

# def square():
#     a=200
#     res=a*a
#     print(res)

# square()

# ex:9 cube of a number
# def square():
#     a=2
#     res=a*a*a
#     print(res)

# square()

# ex_:10 
# def square():
#     a=2
#     res=a*a
#     return(res)
# x=square()
# print(x)

# def cube():
#     a=2
#     res=a*a*a
#     return res
# x=cube()
# print(x)

# ex:10
# def square(a):
#     res=a*a
#     print(res)
# square(10)

# def square(a):
#     res=a*a
#     print(res)
# square()-----------TypeError: square() missing 1 required positional argument: 'a'

# def square(a):
#     res=a*a*a
#     print(res)
# square(3)

# ex:11
# def square(a):
#     res=a*a
#     return res
# x=square(2)
# print(x)

# ex:12 global variable
# x=100
# def test():
#     print(x)

# test()

# ex:13 give the priority to local variable

# x=100
# def test():
#     x=200
#     print(x)
# test()

# ex-14: local variable musst be initialized
# def test():
#     x
#     print(x)--NameError: name 'x' is not defined
# test()

# ex:15 global variables should be initialized 
# x
# def test():
#     print(x)--NameError: name 'x' is not defined
# test()

# ex:16
x=100
def test():
    global x
    x=x+1
    print(x)
print(x)
test()
print(x)