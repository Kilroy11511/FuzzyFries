import pandas as pd
import streamlit as st
import warnings
import plotly.express as px

warnings.filterwarnings("ignore")

st.title("Netflix Analysis")
st.write(
    "Hi, my name is Biya and I am 13 and I go to Boisevain school. I like playing video games and watching anime. I wanted to do AI Camp because it seemed interesting and I am into technology."
)
st.write(
    "My name is Olivia and I am 15 years old. Some of my hobbies are hanging out with my friends and going out with family. I was interested in AI Camp because I've never coded before."
)  #put bios here
st.write(
    "Hi! my name is Thomas and I am 22 years old. I am a mentor at AI Camp. In my free time, I play video games and work out."
)
st.write(
    "My name is Eden I'm currently going to 10th grade I had some prior experience in coding through designing a VR Map for a VR camp not that long ago."
)
st.write(
    "Hello everyone! This is our site called the Fuzzy Fries and the point of this site is to educate ourselves and others on data analysis. The reason why we chose a data set on Netflix is because it is what interested us the most and we want to know if our hypothesis on whether or not people's age affects what kind of subscription they buy is correct."
)
netflix = pd.read_csv(
    'https://raw.githubusercontent.com/Kilroy11511/FuzzyFries/main/Netflix%20Userbase.csv'
)

netflix.drop(["Plan Duration"], axis=1,
             inplace=True)  #only one value in column, irrelevant

st.dataframe(netflix.head())
st.divider()
st.header("Our Graphs")


st.divider()
#for eden's pie chart
ageBins = [25, 30, 35, 40, 45, 50, 55]
labels = ['25-30', '30-35', '35-40', '40-45', '45-50', '50-55']

netflix['Binned Ages'] = pd.cut(netflix['Age'],
                                bins=ageBins,
                                right=True,
                                labels=labels)

basicDF = netflix[netflix['Subscription Type'] == "Basic"]
basicDFVC = basicDF['Binned Ages'].value_counts()
fig = px.pie(basicDFVC,
             values=basicDFVC.values,
             names=basicDFVC.index,
             title='Basic Plan')
st.plotly_chart(fig)

standardDF = netflix[netflix['Subscription Type'] == "Standard"]
standardDFVC = standardDF['Binned Ages'].value_counts()
fig = px.pie(standardDF,
             values=standardDFVC.values,
             names=standardDFVC.index,
             title='Standard Plan')
st.plotly_chart(fig)

premiumDF = netflix[netflix['Subscription Type'] == "Premium"]
premiumDFVC = premiumDF['Binned Ages'].value_counts()
fig = px.pie(premiumDF,
             values=premiumDFVC.values,
             names=premiumDFVC.index,
             title='Premium Plan')
st.plotly_chart(fig)

st.write(
    "The pie charts show that as age increases, the likelihood of them subscribing to a plan however after the age of 50 this chance and likelihood drops sharply for a yet unknown reason."
)

st.divider()

#for thomas' pie chart
planValueCounts = netflix['Subscription Type'].value_counts()
fig = px.pie(netflix,
             values=planValueCounts.values,
             names=planValueCounts.index,
             title="Proportions of Subscription Types")
st.plotly_chart(fig)

st.write(
    "This visualization shows the ratio of different subscription types to each other. We can see basic is 40% of users, with standard at 30.7% and Premium at 29.3%."
)
st.divider()
#for bar chart
netflixGrouped = netflix.groupby(['Subscription Type'
                                  ]).mean(numeric_only=True)['Age']
fig = px.bar(netflix,
             x=netflixGrouped.index,
             y=netflixGrouped.values,
             labels={
                 'x': 'Subscription Type',
                 'y': 'Age'
             },
             title='Mean Age By Subscription Type')
st.plotly_chart(fig)

st.write(
    'This graph represents the subscription types of Netflix users based on their ages. For example, the "Basic" subscription age average is 38.82883, the "Premium" subscription is 38.51296, "Standard" subscription is 39.02214.'
)

st.divider()
#for violin plot
fig = px.violin(
    netflix,
    y='Age',
    x='Subscription Type',
    title='Distribution of Concentration of Age with Subscription Type')
st.plotly_chart(fig)

st.write(
    'This violin plot shows that the "Basic" and "Premium" subscription users are mostly 30 years old. For the "Standard" subscription users, they are in the 40-45 year old range.'
)

st.divider()
#for bar chart

subTypeandAgeVC = netflix.value_counts(['Subscription Type', 'Binned Ages'])
subTypeandAgeDF = subTypeandAgeVC.rename_axis(
    ['Subscription Type', 'Binned Ages']).reset_index(name="Counts")

fig = px.bar(subTypeandAgeDF,
             x='Binned Ages',
             y='Counts',
             color='Subscription Type',
             title="Proportions of Subscription Types to Ages")
st.plotly_chart(fig)

st.write(
    "This is a long format data box chart that shows the subscription type amount for each age group. For ages 35-40, most people use the basic plan and ages 30-35 have the most people using the standard and premium subscription plan."
)

st.divider()
#for box plot
fig = px.box(netflix,
             y="Age",
             x='Subscription Type',
             title='Age and Subscription')
st.plotly_chart(fig)

st.write(
    "This box plot shows the age to subscription type values. For example, the youngest person to use the basic subscription type was 27 years old and the oldest was 45 and the one in the middle was 39."
)

st.divider()
st.header("Conclusion")
st.write(
    "In conclusion, we have discovered that there seems to be a correlation between age and the likeliness of subscribing to a plan. However, there is no correlation between age and the greater likelihood of a person subscribing to a higher rated plan. We can see through all the charts that as the age increases from 20-50 the chances of the person being subscribed to a plan increases however it seems to drop sharply once they go past the page of 50 this is likely due to the fact that they either have a distrust towards technology or don’t know how to operate it properly however this is still a speculation. This is important because this means Netflix should cater more to the middle aged people due to the fact that they mostly make up their main paying demographics."
)
