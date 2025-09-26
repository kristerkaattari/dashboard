import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

data = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS.
  "abdelrahmanemad594/premier-league-season-2024")
df = pd.read_csv(data)
st.write(df.head())


#df = pd.read_csv("PremierLeagueSeason2024.csv", sep=",")
#t.write(df.head())