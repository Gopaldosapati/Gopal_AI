# Keys are immutable and values are mutable
# represented in {}
#before 3.7 version its unordered, now its ordered
#supports hashable and searching is faster
#size is dynamic

# d1={
#     "name":"vpro",
#     "sub":"AgenticAI",
#     "Version":1.0
# }
# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1={}
# print(type(d1))

# d2={
#     (10,20):"Hello"
# }
# print(d2)

#ex:
# d1={
#     "key1":"Hello",
#     "key2":"VPro",
#     "key3":"AgenticAI"
# }

# print(d1)
# d2=dict(key1="hello",key2="welcome")
# print(d2)

# d3=dict([("key1","Hello"),("key2","Welcome")])
# print(d3)

# print(d1.keys())
# print(d1.values())
# print(d1.items())

#ex:
# d1={
#     "key1":"Hello",
#     "key2":"VPro",
#     "key3":"AgenticAI"
# }
# for keys in d1.keys():
#     print(keys)
# for values in d1.values():
#     print(values)
# for key,value in d1.items():
#     print(f"key is:{key} and values is: {value}")

#ex:
# outer={
#     "name":"VPro",
#     "address":{
#         "location":"SR Nagar",
#         "City":"HYD",
#         "Pin":520112
#     }
# }
# print(outer["address"]["location"],outer["address"]["City"],outer.get("address",{}).get("Pin"))

#ex:
# d1={}
# d1["key1"]=100
# d1["key2"]=200
# # print(d1)

# # d1["key1"]=500
# # print(d1)

# #print(d1["key1"])
# #print(d1("key4"))
# d1.pop("key1")
# print(d1)
# d1.popitem()
# print(d1)

#Ex:
# d={
#     "key1":100,
#     "key1":200,
#     "key2":300

# }
# print(d)  #duplicate key wont return

#ex: Copy
# d={
#     "key":[10,20]
# }
# C=d.copy()  #shallow copy
# d["key"].append(30)
# print(d)

#ex  Deep copy
# import copy
# d={
#     "key":[10,20]
# }
# C=copy.deepcopy(d) #shallow copy
# print(C)
# d["key"].append(30)
# print(d)
# print(C)  # wont change

#ex: keys must be hashable
# d={
#     (1,2):[1,2]
# }
# print(d)

# #Ex:
# d={x:x*x for x in range(5)}
# print(d)

#ex:
# d={}
# d[True]=100
# d[1]=1000
# print(d)  # it will overide with latest

#Ex:
# d2={}
# d2[1]=100
# d2[1.0]=1000
# print(d2)

#ex: condition check using in and return True or False
d3={
    "key1":100,
    "key2":200
}
print("key1" in d3)
print("key2" in d3)
print("key3" in d3)

#ex:

