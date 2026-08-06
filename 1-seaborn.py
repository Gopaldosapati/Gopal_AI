#seaborn package is used to styled graph,built on top of matplotlib

# import seaborn as sns
# import matplotlib.pyplot as plt
# tips=sns.load_dataset("tips")  # by using load_dataset read the data from sns library
# data1=tips.head(10)
# sns.lineplot(data=data1,x="size",y="total_bill")
# plt.show()
# #print(tips)
# plt.savefig("seaborn_lineplot.png")

#Ex:
# import seaborn as sns
# import matplotlib.pyplot as plt
# iris=sns.load_dataset("iris")
# iris=(iris.head(10))
# sns.scatterplot(data=iris,x="sepal_length",y="sepal_width",style="species",s=200,hue="species",palette="Set2")
# plt.show()

#Ex:
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips=sns.load_dataset("tips")
# sns.histplot(tips["total_bill"],bins=20,kde=True)  #kde is used to draw curve
# plt.show()


#Ex:
# import seaborn as sns
# import matplotlib.pyplot as plt
# tips=sns.load_dataset("tips")
# sns.boxplot(data=tips,x="day",y="total_bill")
# plt.show()


#Ex:
# import seaborn as sns
# import matplotlib.pyplot as plt
# flights=sns.load_dataset("flights")
# pivot=flights.pivot(index="month",columns="year",values="passengers")
# sns.heatmap(pivot,annot=True,fmt="d",cmap='YlGnBu')
# plt.show()


#Ex:

