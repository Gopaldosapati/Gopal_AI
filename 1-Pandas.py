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
