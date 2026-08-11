#function without name is called as lambda function
#"lambda" is the keyword used to declare a lambda function

# add=lambda a,b:a+b
# res=add(100,200)
# print(res)

# square=lambda a:a*a
# res=square(4)
# print(res)

# cube=lambda a:a*a*a
# res=cube(4)
# print(res)
# print(cube(5))

#ex:1
# even=lambda a:a%2==0
# print(even(10))  #o/p True
# res=even(9)  #o/p False
# print(res)

#ex:2
# large=lambda a,b:a if a>b else b
# print(large(200,100))
# print(large(10,20))

# large=lambda a,b,c:a if (a>b and  a>c) else (b if b>c else c)
# print(large(200,100,50))
# print(large(200,400,100))
