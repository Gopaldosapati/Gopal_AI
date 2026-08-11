# d={
#     "Name":"Gopal",
#     "age":40,
#     "gender":"Male"
# }
# #print(d)
# # print(d.keys())
# # print(d.values())
# print(d["Name"])

# d1=dict(name="Madhuri",age=34,gender="Female")
# print(type(d1))
# # print(d1)
# # print(d1["name"])
# # print(d1.get("location"))
# # print(d1.get("location","hyd"))
# d1["location"]="Hyderabad"
# d1["pin"]=502032
# print(d1)
# #print(d1.pop("location"))
# d1.pop("pin")
# print(d1)
# d1.popitem()
# print(d1)

#d1=dict(apples=10,banana=20,oranges=50)
# for fruit in d1:
#     print(fruit)
# for values in d1.values():
#     print(values)
# for key,values in d1.items():
#     #print(key,values)
#     print(f"fruit name is :{key} and its value is : {values}")
#     print(len(d1))

emp={
    "emp1":{
        "name": "Alice",
        "role": "Developer",
        "skills": ["Python", "SQL"]
    },
    "emp2":{
        "name": "Bob",
        "role": "Designer",
        "skills": ["Figma", "CSS"]
    }
}
#print(emp)
print(emp["emp1"])
print(emp["emp2"]["skills"])