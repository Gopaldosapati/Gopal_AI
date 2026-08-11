# when we pass * to variable in the function is nothing but variable length parameter. 
# If we pass * it conveerted into tuple

# def test (*param1):
#     print(param1)
# test(10,20,30,40)

# ex:2
# def test(*a):
#     print(a)
#     print(type(a))
#     print(len(a))
#     x=a[0]      #x--->HTML
#     y=tuple(x)   #["H","T","M","L"]
#     z=y[::-1]
#     print(z)

# test("HTML","JAVA","ETL",".net")


#ex-3: err:only oe variabe length paraeter can accept through a function
# def test(*a,*b):
#     pass


#ex--4
# order of parameters priority in function definition
# 1)positional parameters
# 2)default parameters
# 3)variable length parameters

# def test(a=100,b,*c):
#     pass
# print(a)--error
    
#ex-6:  keyword length parameters
#if we pass ** t the function parameter, it will be converted to dictionary

# def test(**a):
#     print(type(a))   #<class 'dict'>
# test()

# def test(a,b,*c,**d):
#     print(a,b,c,d)

# test(10,20,30,40,name="hello")    # result: 10 20 (30, 40) {'name': 'hello'}

