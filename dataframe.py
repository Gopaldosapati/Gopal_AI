import pandas as pd
# Employees={
#     "emp1":[101,102,103,104],
#     "Dept":["IT","Finance","HR","Tech"],
#     "Sal":[1000,2000,3000,4000]
# }
# df=pd.DataFrame(Employees)
# print(df)
df=pd.read_csv("employees.csv",header=None)
#filt=df[df["Gender"]=="Male"]
#print(res[res["Salary"]>=50000])
#cnt=df.groupby("Department").size()
#cnt=df.groupby("Department")["Salary"].max()
#cnt=df[df["Department"]=="IT"]["Salary"].max()
#print(res[res["Department"]=="IT"]["Salary"].max())
print(df)