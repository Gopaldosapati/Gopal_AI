#to manipulate all list elements that functions called as map function
#ex [1,2,3]*5=[5,10,15]

# res=list(map(lambda a:a*10,[1,2,3,4]))
# print(res)

# res=list(map(lambda a:a*10,(1,2,3,4)))
# print(res)

res=tuple(map(lambda a:a*10,(1,2,3,4)))
print(res)

res=tuple(map(lambda a:a*10,[1,2,3,4]))
print(res)