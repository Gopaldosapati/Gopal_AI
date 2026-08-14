from fastapi import FastAPI
from pymongo import MongoClient

app=FastAPI()
client=MongoClient("mongodb+srv://admin:admin@vprogopal.ikjmbly.mongodb.net/?appName=VProGopal")
practice_db=client["practice_db"]
student=practice_db["student"]

@app.post("/student")

def create_student(name:str,marks:float,age:int):
    res=student.insert_one({"name":name,"marks":marks,"age":age})
    return {
        "message":"record inserted successfully",
        "id":str(res.inserted_id)
    }


@app.get("/student")
def read_student():
    data=student.find()
    result=[]
    for s in data:
        s["_id"]=str(s["_id"])
        result.append(s)

    return result

@app.get("/student/{name}")
def student_name(name:str):
    record=student.find_one({"name":name})
    if record:
        record["_id"]=str(record["_id"])
        return record
    return {
        "message":"student not available"
    }

@app.put("/student/{name}")
def update_student(name:str,marks:float):
    res=student.update_one({"name":name},{"$set":{"marks":marks}})
    return {
        "msg":"records updated successfully",
        "id":str(res.modified_count)
    }

@app.delete("/student/{name}")
def delete_student(name:str):
    res=student.delete_one({"name":name})
    return {
        "msg":"record deleted successfully",
        "id":res.deleted_count
    }