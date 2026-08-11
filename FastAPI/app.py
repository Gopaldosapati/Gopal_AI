#GET--> reading data from backend
#POST --> sending data to backend
#PUT --> update backend data
#DELETE ----> Delete backend data


#fastapi  #is the library
#uvicorn  #is a light weight server to execute

# from fastapi import FastAPI  #FastAPI is a readymade class
# app=FastAPI()   #need to create an object for that API
# #create a get request

# @app.get("/gop") #"/" #is a empty end point
# def home():
#     return {"msg":"welcome to FastAPI !!!"}

#to execute this need a command like "uvicorn 'name of the file':app --reload"

#Ex:

# from fastapi import FastAPI
# app=FastAPI()

# @app.get("/reg_no")
# def demo_get():
#     return "welcome to get req !!!"

# @app.post("/req1")
# def demo_post():
#     return "welcome to post req !!!"

# @app.put("/req2")
# def demo_put():
#     return "welcome to put req !!!"


#Ex: path parameter

# from fastapi import FastAPI

# app=FastAPI()

# #path parameter
# @app.get("/users/{user_id}")   #users is reference an user_id is parameter
# def demo_pathparam(user_id:int):
#     return user_id

# #Query parameter
# #http://127.0.0.1:8000/search?sub=AgenticAI&page=1'

# @app.get("/search")
# def query_param(sub:str,page:int=1):
#     return f"sub : {sub} and page num is {page}"

# #http://127.0.0.1:8000/gym/100/9865446789'
# @app.get("/gym/{id}/{contact}")
# def gym_data(id:int,contact:int):
#     return f"id is: {id} and ph number is :{contact}"


#ex: Mongo DB integration
#MongoDB is document oriented DB, light weight DB, and NOSQL DB
#tables are equivalent to collections, records are equivalent to documents.

from fastapi import FastAPI
