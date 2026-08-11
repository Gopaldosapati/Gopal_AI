#string is a colletion of characters
# can create a string with double quotes,single quote and tripple quotes
#in creating paragraphs we can use tripple quotes

# wish="welcome"
# print(wish)

# name="VPro"
# print("welcome to ",name)

#adding 2 strings****************************
# name="VPro"
# msg="welcome " + name
# print(msg)

## paragraph message

# msg=""" hello
#         how are you
#         Gopal"""
# print(msg)

#using format (f) calling multiple varibles in the print

# course="Agentic AI"
# version=1.0
# print(f"welcome to {course} and version is {version}")
# name="Rahul"
# age=24
# print("Student name is {} and his age is {}".format(name,age))

#different styles in printing a statement*****************

# print("GenAI\n AgenticAI")
# print("GenAI\t AgenticAI")
# print('GenAI "AgenticAI"')

# print("LLM ","GEN AI",sep="$")
# print("LLM ","GENAI",sep='$')

# to check type of a variable
# name="VPro"
# print(type(name))


#INTEGERS

# num1=200
# num2=300
# add=num1+num2
# sub=num1-num2
# div=num1/num2
# print(num1+num2)
# print("addition of numbers:",add)
# print(f"subtraction of number is {sub}")
# print("division of numbers{}",format(div))

#hexadecimal,octal and binary umbers automatically convert into decimal
# num1=0x1234
# print(num1)

# num2=0o1234
# print(num2)

# print(10%3) #remainder =1
# print(2**3)  #power of :8
# print(10//3)  # floor division we will get the round number: 3
# print(10/5)  #division:2.0

# python able to handle very large numbers as well without truncate

# num1=123456678879900090908754322567899764323489
# print(num1)

#Floating numbers

# num1=10.2
# print(num1)
# print(type(num1))

# num1=243.56479987
# print(round(num1,2))
# print(round(num1,9))
# print(round(num1,0))
# print(round(num1,-100))
# print(f"{num1:.2f}")
# print(format(num1,".2f"))


# num1=0.2
# num2=0.4
# num3=num1+num2
# print(num3)   #0.600000000001  python will give very accurate value


# == is compares two values
# print(10==20)  #false
# print((0.1+0.2)==0.3)  # flase because python always give accurate number on addition

#Boolean values
# True=1 false=0

# flag1=True
# print(flag1)
# print(type(flag1))

# print(True+True)
# print(True+False)
# print(True+False+True)
# print("1"+True)  # cant concate str with number

#Falsy values  : False,none,0.0,[],(),{},set()
#Truthy Values : True,1.0,[10],(10,20),{"hi":10},set(10,20

#Conversions
# num1=27.10
# print(int(num1))   #result =27

# num2="10"
# print(int(num2))   #conversting str to int --ans=20

# print(int(True))  #ans is 1
# print(int(False))  # ans is 0


# x=10
# print(x.bit_length())

