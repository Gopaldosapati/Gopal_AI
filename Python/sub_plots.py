#collaborating multiple graphs into single
#Ex:
# import matplotlib.pyplot as plt
# subjects=["python","c","java","eng"]
# marks=[30,50,26,44]

# plt.figure(figsize=(12,8))

# #lineplot
# plt.subplot(2,2,1)
# plt.plot(subjects,marks,marker='o',linestyle='--')
# plt.title("Line_plot")

# #Bar chart
# plt.subplot(2,2,2)
# plt.bar(subjects,marks,color="orange")
# plt.title("Bar_chart")

# #pie chart
# plt.subplot(2,2,3)
# plt.pie(marks,labels=subjects)
# plt.title("pie_chart")

# plt.show()

# plt.savefig("sub_plot.png")


#Ex: Histoplot( quesstions )
# import matplotlib.pyplot as plt

# marks = [
#     35, 40, 42, 45, 48,
#     50, 52, 55, 58, 60,
#     62, 65, 68, 70, 72,
#     75, 78, 80, 82, 85,
#     88, 90, 92, 95
# ]
# plt.figure(figsize=(12,8))

# plt.hist(
#     marks,
#     bins=6,   #no.of categories
#     edgecolor='black',
#     color='skyblue',
#     linewidth=2,
#     alpha=0.8,
#     histtype='bar',
#     rwidth=0.9,
#     label='students'
# )
# plt.title("student marks distribution",fontsize=18,fontweight="bold")
# plt.xlabel("marks")
# plt.ylabel("students")
# plt.legend()
# plt.show()
# plt.savefig("Hist_plot.png")


#ex:
import matplotlib.pyplot as plt
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]

marks = [35, 42, 50, 60, 68, 75, 88, 95]

# Marker Size
sizes = [80, 100, 120, 140, 160, 180, 200, 220]

# Marker Colors
colors = ['red', 'blue', 'green', 'orange',
          'purple', 'brown', 'pink', 'cyan']

plt.figure(figsize=(10,6))
plt.scatter(study_hours,marks,s=sizes,c=colors,alpha=0.8,edgecolor='black',linewidth=2,label="students")
plt.title("student hours vs marks")
plt.legend()
plt.show()
plt.savefig("scatter.png")