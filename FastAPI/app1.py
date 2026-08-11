from fastapi import FastAPI
from pymongo import MongoClient

#to send get,post,put and delete requests
app=FastAPI()

#connect to mongodb
client=MongoClient("mongodb+srv://admin:admin@vprogopal.ikjmbly.mongodb.net/?appName=VProGopal")

#create database
db=client["cmp_db"]

#table creation
employees=db["employees"]

@app.post("/employees")
def create_emp(name:str,dept:str,salary:float):
    new_emp={
        "name":name,
        "dept":dept,
        "salary":salary

    }
    res=employees.insert_one(new_emp)
    return {
        "message":"employee inserted successfully !!!",
        "id":str(res.inserted_id)
    }

@app.get("/employees")
def read_employees():
        emps = employees.find()

        result = []
        for emp in emps:
            emp["_id"]=str(emp["_id"])
            result.append(emp)

        return result

@app.get("/employees/{name}")
def read_emp(name:str):
        emp = employees.find_one({"name":name})

        if emp:
            emp["_id"] = str(emp["_id"])
            return emp

        return {"msg":"employee not found !!!"}