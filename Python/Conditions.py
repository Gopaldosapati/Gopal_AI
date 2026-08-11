# ex:
# age=18
# if age>=18:
#     print("eligible for vote")

#ex: multiple conditions
# marks=30
# if marks>=90:
#     print("grade A")
# elif marks>=75:
#     print("grade B")
# elif marks>=50:
#     print("grade C")
# else:
#     print("fail")

#ex: Logical AND
# age=19
# location="India"
# if age>=19 and location=='India':
#     print("eligible to vote in India")

#Ex: Not condition
# is_logged= False
# if not is_logged:
#     print("please login")

#Ex: find largest of a number
# a,b,c=50,60,20
# if a>=b and a>=c:
#     print("a")
# elif b>=a and b>=c:
#     print(b)
# else:
#     print(c)

#Ex:
# age=19
# sal=30000
# if age>=18:
#     if sal>=25000:
#         print("eligible for loan")
#     else:
#         print("salary not sufficient")
# else:
#     print("age not sufficient")

#ex:
# a=["python","ML","GenAI","AgenticAI"]
# if "AgenticAI" in a:
#     print("its available")
# else:
#     print("its not available")

# multiple conditions will decrease the performance, it overcome use MATCH.

#Ex:match case
# day=4
# match day:
#     case 0:
#         print("sunday")
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Saturday")
#     case 4:
#         print("Thursday")
#     case _:
#         print("No match")
