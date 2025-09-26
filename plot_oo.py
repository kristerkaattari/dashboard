import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2 , 4, 6, 8, 10]

#Objecr-oriented-rajapinta

fig, ax = plt.subplots()
ax.plot(x, y, label="Line")
ax.set_title("Line chart")
ax.legend()


fig2, ax2 = plt.subplots()
ax2.scatter(x, y, label="Scatter" )
ax2.set_title("Scatter")
ax2.legend()

fig3, ax3 = plt.subplots()
ax3.bar(x, y, label="Bar chart")
ax3.set_title("Bar chart")
ax3.legend()

fig4, ax4 = plt.subplots(3, 1)
ax4[0].plot(x, y, label="Line")
ax4[1].scatter(x, y, label="Scatter")
ax4[2].bar(x, y, label="Bar chart")

fig5, ax5 = plt.subplots(1, 3)
ax5[0].plot(x, y, label="Line")
ax5[1].scatter(x, y, label="Scatter")
ax5[2].bar(x, y, label="Bar chart")

fig6, ax6 = plt.subplots(2, 2)
ax6[0][0].plot(x, y, label="Line")
ax6[0][1].scatter(x, y, label="Scatter")
ax6[1][0].bar(x, y, label="Bar chart")



plt.show()

