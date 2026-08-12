from fastapi import FastAPI
from pymongo import MongoClient,HTTPException
import bcrypt

#to send get,post,put and delete requests
app=FastAPI()

#connect to mongodb
client=MongoClient("mongodb+srv://admin:admin@vprogopal.ikjmbly.mongodb.net/?appName=VProGopal")

#create database
db=client["cmp_db"]

#table creation
employees=db["employees"]

SECRETE_KEY="my-VPro-"


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


@app.put("/employees/{name}/{new_name}/{updated_salary}")
def update_employees(name:str,new_name:str,updated_salary:float):
      res=employees.update_one({"name":name},{"$set":{"name":new_name,"salary":updated_salary}})
      return {
            "message":"record updated successfully",
            "modified_count":res.modified_count
      }

@app.delete("/employees/{name}")
def delete_employee(name:str):
      res=employees.delete_one({"name":name})
      return{"message":"record deleted successfully",
                  "deleted_count":res.deleted_count}