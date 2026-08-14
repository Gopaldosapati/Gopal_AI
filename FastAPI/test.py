# from fastapi import FastAPI
# from pymongo import MongoClient


# app=FastAPI()

# client=MongoClient("mongodb+srv://admin:admin@vprogopal.ikjmbly.mongodb.net/?appName=VProGopal")

# db=client["cmp_db"]
# employees=db["employees"]

# @app.get("/employee/{emp}")
# def get_emp(emp:str):
#     res=employees.find_one({"name":emp})
#     if res:
#         res["_id"]=str(res["_id"])
#         return res
#     return res


# @app.get("/Test/{user_name}/{pwd}")
# def get_req(user:str,pwd:str):
#     return (f"user name : {user} and password is : {pwd}")