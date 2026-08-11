# # import matplotlib.pyplot as plt
# # # ------------------------------------
# # # Student Marks     # medium, 25% 50% 75% max(outlier)
# # # ------------------------------------
# # marks = [
# #     35,40,45,50,55,
# #     60,65,70,75,80,
# #     85,90,95,98,150
# # ]
# # # ------------------------------------
# # # Create Figure
# # # ------------------------------------
# # plt.figure(figsize=(8,6))
# # # ------------------------------------
# # # Box Plot
# # # ------------------------------------
# # plt.boxplot(
# #     marks,
# #     notch=False,  #shape of the figure
# #     vert=True,   #shape ill be inn vertical
# #     patch_artist=True,  #
# #     widths=0.5,
# #     showmeans=True,  # in the figure from mediuam will come arrow symbol states as raising
# #     showfliers=True,  # max value
# #     tick_labels=['Students'],
# #     boxprops=dict(
# #         facecolor='skyblue',
# #         color='blue',
# #         linewidth=2
# #     ),
# #     medianprops=dict(
# #         color='red',
# #         linewidth=3
# #     ),
# #     whiskerprops=dict(
# #         color='green',
# #         linewidth=2
# #     ),
# #     capprops=dict(
# #         color='black',
# #         linewidth=2
# #     ),
# #     flierprops=dict(
# #         marker='o',
# #         markerfacecolor='red',
# #         markersize=20
# #     )
# # )
# # # ------------------------------------
# # # Title
# # # ------------------------------------
# # plt.title(
# #     "Student Marks Analysis",
# #     fontsize=18
# # )
# # # ------------------------------------
# # # Y Label
# # # ------------------------------------
# # plt.ylabel("Marks")
# # # ------------------------------------
# # # Grid
# # # ------------------------------------
# # plt.grid(axis='y')
# # # ------------------------------------
# # # Display
# # # ------------------------------------
# # plt.show()
# # plt.savefig("Box_plot.png")


# #ex:
# import matplotlib.pyplot as plt

# python=[90,120,80,105,130]
# java=[35,79,55,46,75]
# react=[30,20,40,50,70]
# plt.boxplot([python, java, react], patch_artist=True)

# # Add custom x-axis labels
# plt.xticks([1, 2, 3], ["Python", "Java", "React"])

# plt.title("Programming Language Score Distribution", fontsize=16, fontweight="bold")
# plt.ylabel("Scores")
# plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    'Python':[95,90,60,98],
    'Java':[80,85,75,92],
    'SQL':[70,75,65,88]
},
index=['Student A',
       'Student B',
       'Student C',
       'Student D']
)
plt.figure(figsize=(8,6))
sns.heatmap(
    df,
    annot=True,
    cmap='YlGnBu',         #coolwarm viridis Blues Greens Reds YlGnBu magma plasma
    linewidths=1, 
    linecolor='black',
    fmt='d',            # d .1f .2f
    cbar=True
)
plt.title("Student Marks Heatmap")
plt.show()
plt.savefig("Heat_map.png")