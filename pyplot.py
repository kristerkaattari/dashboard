import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


x = [1,2,3,4,5]
y = [2,3,6,7,10]

#Pyplot-rajapinta

plt.figure()
plt.plot(x, y, label="Line") #line chart / plot
plt.title("Line chart")
plt.legend()

plt.figure()
plt.scatter(x, y, label="Scatter") #Scatter chart
plt.title("Scatter plot")
plt.legend()

plt.figure()
plt.bar(x,y, label="Bars")
plt.title("Bar chart")
plt.legend()


plt.show()