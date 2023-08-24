import pandas as pd
import streamlit as st
import warnings
import plotly.express as px

warnings.filterwarnings("ignore")

st.title("Netflix Analysis")
st.write("") #put bios here
st.write("Hello everyone! This is our site called the Fuzzy Fries and the point of this site is to educate ourselves and others on data analysis. The reason why we chose a data set on Netflix is because it is what interested us the most. We want to know if our hypothesis on whether or not people's age affects what kind of subscription they buy is correct.")
netflix = pd.read_csv('https://raw.githubusercontent.com/Kilroy11511/FuzzyFries/main/Netflix%20Userbase.csv')

netflix.drop(["Plan Duration"], axis=1, inplace=True) #only one value in column, irrelevant

st.dataframe(netflix.head())


#for thomas' pie chart
planValueCounts = netflix['Subscription Type'].value_counts()
fig = px.pie(netflix, values=planValueCounts.values, names=planValueCounts.index, title="Proportions of Subscription Types")
st.plotly_chart(fig)

st.write("This visualization shows the ratio of different subscription types to each other. We can see basic is 40% of users, with standard at 30.7% and Premium at 29.3%.")

#for eden's pie chart
ageBins = [25, 30, 35, 40, 45, 50, 55]
labels = ['25-30', '30-35', '35-40', '40-45', '45-50', '50-55']

netflix['Binned Ages'] = pd.cut(netflix['Age'], bins=ageBins, right=True, labels=labels)

basicDF = netflix[netflix['Subscription Type'] == "Basic"]
basicDFVC = basicDF['Binned Ages'].value_counts()
fig = px.pie(basicDFVC, values=basicDFVC.values, names=basicDFVC.index, title='Basic Plan')
st.plotly_chart(fig)

standardDF = netflix[netflix['Subscription Type'] == "Standard"]
standardDFVC = standardDF['Binned Ages'].value_counts()
fig = px.pie(standardDF, values=standardDFVC.values, names=standardDFVC.index, title='Standard Plan')
st.plotly_chart(fig)

premiumDF = netflix[netflix['Subscription Type'] == "Premium"]
premiumDFVC = premiumDF['Binned Ages'].value_counts()
fig = px.pie(premiumDF, values=premiumDFVC.values, names=premiumDFVC.index,title='Premium Plan')
st.plotly_chart(fig)

st.write("The pie charts show that as age increases, the likelihood of them subscribing to a plan however after the age of 50 this chance and likelihood drops sharply for a yet unknown reason.")

#for bar chart
netflixGrouped = netflix.groupby(['Subscription Type']).mean(numeric_only=True)['Age']
fig = px.bar(netflix, x=netflixGrouped.index, y =netflixGrouped.values, labels={'x':'Subscription Type', 'y': 'Age'}, title='Mean Age By Subscription Type')
st.plotly_chart(fig)

st.write('This graph represents the subscription types of Netflix users based on their ages. For example, the "Basic" subscription age average is 38.82883, the "Premium" subscription is 38.51296, "Standard" subscription is 39.02214.')

#for violin plot
fig = px.violin(netflix, y='Age', x='Subscription Type', title='Distribution of Concentration of Age with Subscription Type')
st.plotly_chart(fig)

st.write('This violin plot shows that the "Basic" and "Premium" subscription users are mostly 30 years old. For the "Standard" subscription users, they are in the 40-45 year old range.')

#for bar chart

subTypeandAgeVC = netflix.value_counts(['Subscription Type', 'Binned Ages'])
subTypeandAgeDF=subTypeandAgeVC.rename_axis(['Subscription Type', 'Binned Ages']).reset_index(name="Counts")

fig = px.bar(subTypeandAgeDF, x='Binned Ages', y='Counts', color='Subscription Type', title="Proportions of Subscription Types to Ages")
st.plotly_chart(fig)

st.write("This is a long format data box chart that shows the subscription type amount for each age group. For ages 35-40, most people using the basic plan and 30 - 35 has the most people using the standard and premium subscription plan.")

#for box plot
fig = px.box(netflix, y="Age", x='Subscription Type', title='Age and Subscription')
st.plotly_chart(fig)

st.write("This box plot shows the age to subscription type values. For example, the youngest person to use the basic subscription type was 27 years old and the oldest was 45 and the one in the middle was 39.")