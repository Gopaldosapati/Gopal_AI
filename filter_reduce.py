#filter is used to apply condition
# res=list(filter(lambda a:a%2==0,[1,2,3,4,5])) 
# print(res)

#reduce is used to sum of all the elements in a list

from functools import reduce
res=reduce(lambda a,b:a+b,[1,2,3,4,5])
print(res)