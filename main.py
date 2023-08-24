import pandas as pd
import streamlit as st
import warnings
import plotly.express as px

warnings.filterwarnings("ignore")

st.title("Netflix Analysis")

netflix = pd.read_csv('https://raw.githubusercontent.com/Kilroy11511/FuzzyFries/main/Netflix%20Userbase.csv')

netflix.drop(["Plan Duration"], axis=1, inplace=True) #only one value in column, irrelevant
netflix.head()

fig = px.box(netflix, y="Age", x='Subscription Type')
st.plotly_chart(fig)

#for bar chart
st.write('This graph represents the subscription types of Netflix users based on their ages. For example, the "Basic" subscription age average is 38.82883, the "Premium" subscription is 38.51296, "Standard" subscription is 39.02214.')

#for violin plot
st.write('This violin plot shows that the "Basic" and "Premium" subscription users are mostly 30 years old. For the "Standard" subscription users, they are in the 40-45 year old range.')

#for bar chart
st.write("This is a long format data box chart that shows the subscription type amount for each age group. For ages 35- 40 has the most people using the basic plan and 30 - 35 has the most people using the standerd and premium subcription plan.")