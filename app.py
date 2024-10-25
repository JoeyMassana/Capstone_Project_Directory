# Import packages
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title('Analysis of Employee Attrition & Performance')

# Description
st.write(
    'This project delves into the trends of employee attrition and '
    'performance through comprehensive data analysis using a '
    'pre-generated dataset imported from Kaggle. By exploring '
    'various factors, including job satisfaction, '
    'training opportunities, and years since last promotion, '
    'I gained insights that would be used to guide '
    'organizations in improving employee retention and '
    'performance. The analysis will be visualized through '
    'interactive dashboards, enabling potential stakeholders to '
    'assess satisfaction levels among employees who have left '
    'the organization compared to those who have stayed.'
)

# Created DataFrames
pr_df = pd.read_csv('PerformanceRating.csv')
emp_df = pd.read_csv('Employee.csv')
rt_lvl = pd.read_csv('RatingLevel.csv')

# Merged Ratings dimensional tables with main DataFrame
mstr_df = pd.merge(
    pr_df,
    rt_lvl,
    how='left',
    left_on='EnvironmentSatisfaction',
    right_on='RatingID'
)

merged_df = mstr_df.merge(
    emp_df,
    how='outer',
    on='EmployeeID'
)

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
NullEmployees = (merged_df['Performance ID']
                 .isnull()
                 .sum())


# Title of Section
st.title('Satisfaction Ratings For Employees')

# Description of findings using the satisfaction levels.
st.write('Description of findings using the satisfaction levels.')

# Radio button for selecting which column to display
Ratings = st.radio(
    'Select a column to display:',
    options=['Environment Satisfaction',
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
ax[0].set_ylim(0, 800)
ax[0].set_title('Employees Who Left')
ax[0].tick_params(axis='y', rotation=45)

ax[1].set_xlabel('Ratings')
ax[1].set_ylim(0, 1500)
ax[1].set_title('Employees Who Stayed')
ax[1].tick_params(axis='y', rotation=45)

# Display the histogram in Streamlit
st.pyplot(fig)
plt.show()


# Write title for opportunities bar plot
st.title("Comparison of Training Opportunities Offered vs Taken")

# Description of section
st.write('Description of section')

# Radio button to toggle between two DataFrames
option = st.radio("Select DataFrame to display:",
                  ('Employees Who Left', 'Employees Who Stayed'),
                  key='dataframe_selection_1')

# Select the appropriate DataFrame based on user input
if option == 'Employees Who Left':
    selected_df = df_left
else:
    selected_df = df_sty

# Grouping data by department
grouped_data = (selected_df[
    ['Department',
     'Training Opportunities Within Year',
     'Training Opportunities Taken']
     ]
     .groupby('Department')
     .sum()
     .reset_index()
)

# Melt the data for seaborn compatibility
melted_data = pd.melt(
    grouped_data,
    id_vars='Department',
    value_vars=[
        'Training Opportunities Within Year',
        'Training Opportunities Taken'
    ],
    var_name='Training Type',
    value_name='Count'
)

# Create the bar plot
plt.figure(figsize=(12, 6))
sns.barplot(
    x='Department',
    y='Count',
    hue='Training Type',
    data=melted_data
)

# Customize the plot
plt.title('Comparison of Training Opportunities Offered vs Taken')
plt.xlabel('Department')
plt.ylabel('Count')
plt.ylim(0, 7000)  # Set y-axis limits
plt.legend(title='Training Offered vs Taken')
plt.tight_layout()

# Show the plot
st.pyplot(plt)


# Write title for years before promotion histogram
st.title("Years Before Promotion of Employees Who Left and Stayed")

# Description of section
st.write('Description of section')

# Radio button to toggle between two DataFrames with a unique key
option = st.radio(
    "Select DataFrame to display:",
    ('Employees Who Left', 'Employees Who Stayed'),
    key='dataframe_selection_2'
)

# Select the appropriate DataFrame based on user input
if option == 'Employees Who Left':
    selected_df = df_left
else:
    selected_df = df_sty

# Create a new figure
plt.figure()

# Create histogram
plt.hist(selected_df['Years Since Last Promotion'], bins=10, edgecolor='black')

# Add labels and title
plt.xlabel('Years Since Last Promotion')
plt.ylabel('Number of Employees')
plt.title('Years Since Last Promotion')

# Show the plot
st.pyplot(plt)