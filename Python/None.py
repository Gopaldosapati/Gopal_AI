# None represent empty value or no value

# salary=None
# print(type(salary))
# salary=10000
# print(salary)


# swapping numbers
# a,b=10,20
# a,b=b,a
# print(a)
# print(b)

# value assigned to same lists and if we assigned one list and other also got maodified.
# list1=list2=[]
# print(list1)
# print(list2)
# list1.append(100)
# print(list1)
# print(list2)


#== compares valuees
# is --compares memory location

# l1=[10,20,30]
# l2=[10,20,30]
# print(l1==l2)--values are same so it will return True
# print(l1 is l2)---memory locations are different so result is False

# x=100
# del x
# print(x)--return error like name x is not defined

# x=100
# def test():
#     x=2
#     x=x+1
#     print(x)
# test()
# print(test())


x=10
def test():
    global x
    x+=20
    print(x)
test()
print(x)