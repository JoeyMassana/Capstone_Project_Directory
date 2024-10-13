# Import packages
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("This is a title")

# Description
st.write(
    "This is the description of the dataset I am using and some of the initial findings about it."
    )

# Created and merged DataFrames.
pr_df = pd.read_csv('PerformanceRating.csv')
emp_df = pd.read_csv('Employee.csv')
merged_df = pr_df.merge(emp_df, how='outer', on='EmployeeID')

# Rename columns
merged_df.rename(
    columns={
        'PerformanceID': 'Performance ID',
        'EmployeeID': 'Employee ID',
        'ReviewDate': 'Review Date',
        'EnvironmentSatisfaction': 'Environment Satisfaction',
        'JobSatisfaction': 'Job Satisfaction',
        'RelationshipSatisfaction': 'Relationship Satisfaction',
        'TrainingOpportunitiesWithinYear': 'Training Opportunities Within Year',
        'TrainingOpportunitiesTaken': 'Training Opportunities Taken',
        'WorkLifeBalance': 'Work-Life Balance',
        'SelfRating': 'Self Rating',
        'ManagerRating': 'Manager Rating',
        'FirstName': 'First Name',
        'LastName': 'Last Name',
        'BusinessTravel': 'Business Travel',
        'DistanceFromHome (KM)': 'Distance From Home (KM)',
        'EducationField': 'Education Field',
        'JobRole': 'Job Role',
        'MaritalStatus': 'Marital Status',
        'StockOptionLevel': 'Stock Option Level',
        'OverTime': 'Over Time',
        'HireDate': 'Hire Date',
        'YearsAtCompany': 'Years At Company',
        'YearsInMostRecentRole': 'Years In Most Recent Role',
        'YearsSinceLastPromotion': 'Years Since Last Promotion',
        'YearsWithCurrManager': 'Years With Current Manager'
    },
    inplace=True
)

# Display a dataframe as an interactive table in Streamlit.
df = st.dataframe(merged_df)

# Calculated number of employees with no performance data.
NullEmployees = merged_df['Performance ID'].isnull().sum()

# Streamlit app
st.title('Satisfaction Ratings For Employees')

# Description of findings using the satisfaction levels.
st.write('Description of findings using the satisfaction levels.')

# Radio button for selecting which column to display
Ratings = st.radio(
    'Select a column to display:',
    options=[
        'Environment Satisfaction',
        'Job Satisfaction',
        'Relationship Satisfaction'
        ],
    index=0  # Default to the first column
    )

# Created DataFrame of employees who left
df_left = merged_df[merged_df['Attrition'] == 'Yes']

# DataFrame of employees who stayed
df_sty = merged_df[merged_df['Attrition'] == 'No']

# Create a histogram for the selected column
fig, ax = plt.subplots(ncols=2)
ax[0].hist(df_left[Ratings], bins=5, color='skyblue', alpha=0.7)
ax[1].hist(df_sty[Ratings], bins=5, color='skyblue', alpha=0.7)

ax[0].set_xlabel('Ratings')
ax[0].set_ylabel('Employees')
ax[0].set_title('Employees Who Left')

ax[1].set_xlabel('Ratings')
ax[1].set_title('Employees Who Stayed')

# Display the histogram in Streamlit
plt.yticks(rotation=45)
st.pyplot(fig)
plt.show()