#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

salary = pd.read_csv("Salary.csv")

st.markdown("""<style>.big-font {font-size:40px !important;} </style> """, unsafe_allow_html=True)
'''
# Joseph Chang
# DATA 200 Assignment 3
'''
st.markdown("""<style>.big-font {font-size:40px !important;} </style> """, unsafe_allow_html=True)
#st.markdown('<p class="big-font"> DATA 200 Assignment 3</p>', unsafe_allow_html=True)

name = st.text_input('What is your name?')
if name:
    st.write(f'Hello {name}! Take a look at my charts!')

    st.markdown("""<style>.big-font {font-size:30px !important;} </style> """, unsafe_allow_html=True)
    st.markdown('<p class="big-font"> This is the dataset I used. Let\
    us see if we can extract meaningful insights: </p>'\
    , unsafe_allow_html=True)
    st.dataframe(salary)
    st.write("There are 6704 rows and 6 columns.")

    if st.button("Click here to see the summary statistics"):
        st.dataframe(salary.describe())
        st.write("This dataframe shows just the numerical columns of just Age, \
    Years of Experience, and Salary.")

'''
# Research Problem
'''
st.write("This goal of this report is to extract meaning insights and identify trends\
    of salaries of people. This dataset is contains information \
    such as age, gender, educational level, job, years of experience, and s\
    alary. The following contains a variety of graphs\
    such as bar plot, scatterplot, pie chart, boxplot. As current students \
    completing their master's degree in data analytics, I want to see what the\
    average salary would be given certain factors. It should be noted the data\
    may not represent actual data.")


'''
# Graph 1: Histogram of Salary
'''
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a histogram: </p>', unsafe_allow_html=True)
sal = salary[salary['Job Title'] == 'Data Analyst']
fig, ax = plt.subplots()
ax.hist(sal['Salary'], edgecolor = "black")
ax.set_title("Histogram of Salary")
ax.set_xlabel('Salary Value')
ax.set_ylabel('Count')
st.pyplot(fig)
st.write("This histogram showing salary. Since there are many job titles in the data\
    I have filtered to just Data Analyst. The histogram organizes the salary into\
    groups. It doesn't appear there is an immediate trend we can infer. Some possib\
    ilities include normal or left-skewed. Most salaries fall between 90k to 100k.")

'''
# Graph 2: Pie chart of Job Title Counts
'''
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a stem plot: </p>', unsafe_allow_html=True)
entry = salary[salary['Years of Experience'] < 3]
data = entry.groupby(['Job Title']).agg({'Salary': ['mean', 'count']}).reset_index()
data.columns = ['Job Title', 'Mean Salary', 'Salary Count']
top_10 = data.sort_values(by='Salary Count', ascending=False).head(8)
st.dataframe(top_10)
st.write("This is the dataframe showing average salary and count of each job title.\
    The mean salary for Data Analysts is almost 100k.")
job_title_counts = top_10['Job Title'].value_counts()
fig, ax = plt.subplots()
ax.pie(top_10['Salary Count'], labels=top_10['Job Title'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)
st.write('This is a simple pie chart based on job title counts. Note that this is just for \
    entry level candidates. So, the years of experience is below 3 years. We see that \
    Junior Sales Associate is the most common job at 142 or 21.1%, \
    followed by Data Analysts at 18.7%')
         
'''
# Graph 3: Bar Chart of each Gender and Education Level on Salary
'''
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a bar graph: </p>', unsafe_allow_html=True)
sal = salary[salary['Job Title'] == 'Data Analyst']
data = sal.groupby(['Gender', 'Education Level'])['Salary'].mean()
df = pd.DataFrame(data, columns=['Salary']).reset_index()
fig, ax = plt.subplots()
pivot_data = df.pivot(index='Education Level', columns='Gender', values='Salary')
colors = {'Male': 'blue', 'Female': 'pink', 'Other': "orange"}
pivot_data.plot(kind='bar', ax=ax, rot=0, color=[colors[column] for column in pivot_data.columns])
ax.set_xlabel('Education Level')
ax.set_ylabel('Average Salary')
ax.set_title('Average Salary Based on Gender and Education Level')
plt.xticks(rotation=90, ha="right")
st.pyplot(fig)
st.write("This bar graph shows the average salary for each gender and broken down by education\
    level. Again, the data has been filtered to data analysts. We see that \
    males tend to earn more if the degree is bachelors. For master's degrees, \
    we see females earning more than males on average.")

    
'''
# Graph 4: Line Chart of Average Salary based on Experience
'''
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a boxplot: </p>', unsafe_allow_html=True)
sal = salary[salary['Job Title'] == 'Data Analyst']
data = sal.groupby(['Years of Experience'])['Salary'].mean().reset_index()
fig, ax = plt.subplots()
ax.plot(data['Years of Experience'], data['Salary'], marker='o', label='Line Chart')
ax.set_title("Line Chart of Average Salary on Experience")
ax.set_xlabel('Years of Experience')
ax.set_ylabel('Average Salary')
st.pyplot(fig)
st.write("This shows average salary for each number of years of experience for Data Analysts only.\
    We see that for data analysts, average salary increases from 0 to 5 years. From year 6 to\
    8, it decreases. After year 8, the average salary increases again tremendously to 160k.\
    Then it falls back down, but this may be due to outlier.")

'''
# Graph 5: Scatterplot of Experience vs Salary
'''
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a scatterplot graph: </p>', unsafe_allow_html=True)
sal = salary[salary['Job Title'] == 'Data Analyst']
fig, ax = plt.subplots()
ax.scatter(sal['Years of Experience'], sal['Salary'])
ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary")
ax.set_title("Experience vs Salary")
st.pyplot(fig)
st.write("This scatterplot shows the experience level in years vs the salary for each year.\
    Just like the histogram, the data has been filtered to job titles of Data Analysts.\
    We see that there is a positive trend. With more years of experience, the \
    more salary a person will earn. There is one outlier at around 13 years \
    of experience but earning just around 80k yearly.")

'''
# Graph 6: Scatterplot of Age vs Salary
'''
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a scatterplot graph: </p>', unsafe_allow_html=True)
sal = salary[salary['Job Title'] == 'Data Analyst']
fig, ax = plt.subplots()
ax.scatter(sal['Age'], sal['Salary'])
ax.set_xlabel("Age")
ax.set_ylabel("Salary")
ax.set_title("Age vs Salary")
st.pyplot(fig)
st.write("This is another scatterplot of the age vs the salary. Again, the data\
    is filtered to Data Analysts. We see that like the previous scatterplot,\
    the trend is positive. The more age, the more salary a person will earn.\
    We see the outlier exists again: the person earning 80k was around 41 years of age.")



'''
# Graph 7: Boxplot of Salary
'''
st.markdown("""<style>.big-font {font-size:16px !important;} </style> """, unsafe_allow_html=True)
st.markdown('<p class="big-font"> Here is a boxplot: </p>', unsafe_allow_html=True)
sal = salary[salary['Job Title'] == 'Data Analyst']
fig, ax = plt.subplots()
ax.boxplot(sal['Salary'])
ax.set_title("Boxplot of Salary")
ax.set_xlabel('Salary')
ax.set_ylabel('Value')
st.pyplot(fig)
st.write("This shows a boxplot of salary for Data Analyst. The 25th percetile is \
    around 100k. The median or 50th percentile is around 120k. \
    The 75th percentile is around 140k, and there are two outliers we see as well.")
