#library name is matplotlib used to draw below graphs
# lineplot,graph,bar,pi,hist,subplot etc

# import matplotlib.pyplot as plt
# months=["jan","Feb","Mar","Apr","May","Jun"]  #x-axis
# sales=[100,160,200,180,250,220]         #y-axis
# #create a figure 
# plt.figure(figsize=(10,6))

# #draw the line plot using plot keyword
# plt.plot(months,sales,linestyle="--",color="Blue",linewidth=3,marker="o",markersize=10,
#          markerfacecolor="yellow",
#          markeredgecolor="red",
#          markeredgewidth=3,
#          label="monthly sales")
# plt.title("line Plot Demonstration")
# plt.legend() # used to diplay lebel in the plot
# plt.grid(True)
# plt.xlabel("months",fontsize=12)
# plt.ylabel("sales",fontsize=12)
# #plt.xlin('jan','Jun')
# plt.annotate(
#     "Highest Sales",
#     xy=("Jun",250),
#     xytext=("may",278),
#     arrowprops=dict(facecolor="black")
# )
# plt.savefig("Line_plot.png")
# plt.show()

#ex:multiline 
import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may","jun"]
sales=[100,200,300,400,500,600]
profits=[10,20,12,15,17,18]
