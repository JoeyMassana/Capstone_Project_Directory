# Import packages
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Created and merged DataFrames.
pr_df = pd.read_csv('PerformanceRating.csv')
emp_df = pd.read_csv('Employee.csv')
merged_df = pr_df.merge(emp_df, how='outer', on='EmployeeID')

# Rename columns
merged_df.rename(columns={'PerformanceID': 'Performance ID',
                          'EmployeeID': 'Employee ID',
                          'ReviewDate': 'Review Date',
                          'EnvironmentSatisfaction': 'Environment Satisfaction',
                          'JobSatisfaction': 'Job Satisfaction',
                          'RelationshipSatisfaction': 'Relationship Satisfaction',
                          'TrainingOpportunitiesWithinYear': 'Training Opportunities With in Year',
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
                          'YearsWithCurrManager': 'Years With Current Manager'},
                          inplace=True)

# Display a dataframe as an interactive table in Streamlit.
df = st.dataframe(merged_df)

# Calculated number of employees with no performance data.
NullEmployees = merged_df['Performance ID'].isnull().sum()

