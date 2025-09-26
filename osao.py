import pandas as pd
import streamlit as st

df = pd.read_csv("ostot.csv", sep=",")

df.rename(columns={"VEROTON RIVIN OSUUS":"Osto"}, inplace=True) # Muutta taulukon otsikon 

#print(df.head()) # Tulostaa ensimmäiset rivit datakehyksestä
st.write(df.head()) # nettiin

#print(df.tail()) # Tulostaa viimeiset rivit datakehyksestä
st.write(df.tail()) # nettiin

st.write("Dataframen metodeja ja attribuutteja") # Otsikko
st.write("Ensimmäiset rivit", df.head()) #Ensimmäiset viisi riviä
st.write("Datan kuvailu", df.describe()) #Mumeerisen datan kuvailu
st.write("Datan koko, elementtien lkm (rivit * sarakkeet)", df.size)
st.write("Sarakkaiden lukumäärä", len(df.columns))
st.write("Aksikset", df.axes)
st.write(df.dtypes) # Sarakkeiden tietotyypit
st.write(df.shape)  # Rivien ja sarakkeiden määrä (rivimäärä, sarakemäärä)
st.write(df.columns) # Sarakkeiden nimet
st.write(df.index) # Indeksi
st.write(df["Toimittaja"]) # Vain yksi sarake
st.write(df[['Y-tunnus', 'Toimittaja''']].head()) # Vain tietyt sarakkeet 5 ensimmäistä
st.write(df.iloc[:3, :4]) # Ensimmäiset 3 riviä ja 4 saraketta

ostot = df["Osto"]
ostot #magic - sama kun st.write

st.write("Yhteenlaskettu ostojen määrä", round(ostot.sum(),2))

toimittajat = df["Toimittaja"]

yhdistetty = pd.concat([ostot, toimittajat], axis=1)

yhdistetty 

ostot_sum = yhdistetty.groupby("Toimittaja")["Osto"].sum()
st.dataframe(ostot_sum)

lista_toimittajat = df["Toimittaja"].unique()

st.write("Toimittajalista", lista_toimittajat, len(lista_toimittajat))

valinta = st.selectbox(
    "Valitse toimittaja:",
    lista_toimittajat
)

keskiarvo = df[df["Toimittaja"] == valinta]["Osto"].mean()

st.write("Toimittajan ", valinta, "ostosten keskiarvo:", round(keskiarvo,2))

ostot_sum.to_csv("toimittajat_ostot.csv", sep=";", decimal=".")
         




