import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

x = ["tammi","helmi", "maalis", "huhti", "touko", "kesä"]
y = [20, 45, 60, 87 , 100, 120]

fig1 = plt.figure()
plt.plot(x, y, label="Line")
st.pyplot(fig1)

fig2 = plt.figure()
plt.scatter(x, y, label="Scatter plot")
st.pyplot(fig2)

fig3 = plt.figure()
plt.bar(x, y, label="Bar chart")
st.pyplot(fig3)

fig4 = plt.figure()
plt.pie(y, labels=x, autopct="%.2f%%")
st.pyplot(fig4)


df = pd.read_csv("ostot.csv")

df.rename(columns={"VEROTON RIVIN OSUUS":"osto"}, inplace=True)
          
lista = df["TILIN NIMI"].unique()

lista

ostot = df[["osto", "Toimittaja", "TILIN NIMI"]]

ostot_sum = ostot.groupby("TILIN NIMI")["osto"].sum()

ostot_sum

fig = plt.figure()
plt.bar(ostot_sum.index, ostot_sum)
plt.xticks(rotation=90, fontsize=5)
st.pyplot(fig)





