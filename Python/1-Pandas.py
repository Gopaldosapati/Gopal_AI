#pandas library used for data analysis
#Used to clean data
#Used for data transformation
#Used for data visualization like charts,graphs,scatter plot etc
#Used to handling tabular data
#Handle csv/parquet/json

# pip install pandas

 #   or

# create requirements.txt and put pandas inside it.

# pip install -r requirements.txt

# import pandas as pd
# print(pd.__version__)

#Ex:

# import pandas as pd
# data=[10,20,30,40]
# res=pd.Series(data)
# print(res)
# print(res[1])

#ex:
# import pandas as pd
# data=[1,2,3,4,5]
# res=pd.Series(data,index=["std1","std2","std3","std4","std5"])
# print(res["std3"])

#ex: deal with more lists--to convert lists into tablular form we need to use dataFrame function
# import pandas as pd
# Employees={
#     "emp1":[101,102,103,104],
#     "Dept":["IT","Finance","HR","Tech"],
#     "Sal":[1000,2000,3000,4000]
# }
# res=pd.DataFrame(Employees)
# print(res)

#Ex:
import pandas as pd
res=pd.read_csv("employees.csv")
#print(res)
# print(res.head())   #default 5 rows it will return
# print(res.head(2))
# print(res.columns)
# print(res.info())
#print(res[["EmpID","Name","Age"]])
#print(res.describe())   # will retrun count,mean.std,min,25% max,75%,50% details of each column
#print(res.)
#print(res[res["Salary"]>=50000])
#print(res[(res["Salary"]>50000) & (res["Salary"]<=100000)] & (res["Age"]>30))
# print(res.sort_values("Salary"))
# print(res.sort_values("Salary",ascending=False))   #Descending order
#print(res.groupby("Department")["Salary"].max()) 

#print(res[res["Department"]=="IT"]["Salary"].max())
#print(res["Name"].str.upper())

#--------------------2026-07-30----------------------------

# import pandas as pd
# df=pd.read_csv("employees_simple.csv")
# print(df)
# # print(df.to_string(index=False))  #removing default indexes
# print(df.set_index("Name",inplace=True))  # acts a index
#print(df.loc[0:1])  #returns first 2 records. 0 include and 1 also include
# print(df.loc[0,"Salary"])  #row label and column definition
# print(df.iloc[2,2])
# print(df.iloc[0:2])  #iloc is used to return 0 include and 2 exclude
#print(df.set_index("Name"))  #using set_index we can set any column as a index
#print(df.loc[:,["Name","Salary"]])
#print(df.loc[2:,["Name","Salary"]])   #index 2 row with Name and Salary columns
#print(df.loc[0:1:,["Name","Salary"]])  #0,1 index with Name and Salary columns

#Ex:
import pandas as pd
# employees={
#     "empid":[101,102,103,104,105],
#     "Dept":["IT","HR","Finance","Tech","Admin"],
#     "Salary":[10000,20000,15000,18000,13000],
#     "Exp":[2,5,4,6,3],
#     "Name":["Sam","Jhon","Ellen","Mike","Don"]
# }
# df=pd.DataFrame(employees)
# print(df)
# print(df.sort_values("Salary",ascending=False))
#print(df.sort_values(by=["Dept","Salary"],ascending=(False,False)))
#print(df.sort_values("Salary",ascending=False).head(1))  #Highest salary
#print(df.groupby("Dept")["Salary"].sum())
#print(df.groupby("Dept")["Salary"].agg(["min","max","sum","mean","count()"]))

#Ex:

# import pandas as pd
# emps = {

#     "EmpID" : [101,102,103,104,105],

#     "Name" : ["Sam","John","David","Priya","Anjali"]

# }

# salaries = {

#     "EmpID" : [101,102,103,104,106],

#     "Salary" : [55000,70000,45000,90000,60000]

# }
# df1=pd.DataFrame(emps)
# df2=pd.DataFrame(salaries)
#print(pd.merge(df1,df2,on="EmpID"))
# print(pd.merge(df1,df2,on="EmpID",how="left"))
# print(pd.merge(df1,df2,on="EmpID",how="right"))
#print(pd.merge(df1,df2,on="EmpID",how="outer"))

#Ex: to concate rows data we have to use concat function 
#column wise concat by using axis=1

# print(pd.concat([df1,df2]))
# print(pd.concat([df1,df2]),axis=True)


#ex: calculate annual salary
# import pandas as pd
# employees={
#     "empid":[101,102,103,104,105],
#     "Dept":["IT","HR","Finance","Tech","Admin"],
#     "Salary":[10000,20000,15000,18000,13000],
#     "Exp":[2,5,4,6,3],
#     "Name":["Sam","Jhon","Ellen","Mike","Don"]
# }
# df=pd.DataFrame(employees)
# # df["Annual_Salary"]=df["Salary"]*12  #addding new column
# # print(df)

# df.drop("Exp",axis=1,inplace=True)
# print(df)

#Ex:
# import pandas as pd
# df=pd.read_csv("employees_null.csv")
# #print(df)
# # print(df.isnull())
# #print(df.isnull().sum())
# #print(df.fillna({"Age": 0}))  # replace null with 0 in Age column
# print(df["Salary"].fillna(df["Salary"].mean(),inplace=True))


#--------------------------31/07---------------------

#Ex:
import pandas as pd
df1 = pd.DataFrame({

    "EmpID":[101,102,103,104],

    "Name":["Sam","John","David","Priya"],

    "Salary":[50000,60000,70000,80000]

})

df2 = pd.DataFrame({

    "EmpID":[101,102,103,105],

    "Name":["Sam","John","David","Anjali"],

    "Salary":[50000,65000,70000,90000]

})

# print(df1. equals(df2))
# print(df1.compare(df2))
# print(df1.merge(df2,how="left",indicator=True))

#Ex: outer
# res=df1.merge(df2,on="EmpID",how="outer",suffixes=("old","new"))
# print(res)

data = {

    "Employee": ["Sam", "John", "Sam", "David", "John", "David"],

    "Department": ["IT", "HR", "IT", "HR", "IT", "IT"],

    "Salary": [50000, 60000, 55000, 45000, 65000, 70000]

}

df = pd.DataFrame(data)

print(df)
values=df.pivot_table(
    values="Salary",
    index="Employee",
    columns="Department"

)
print(values)