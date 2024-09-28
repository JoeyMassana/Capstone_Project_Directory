# Import packages
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Created and merged DataFrames.
pr_df = pd.read_csv("PerformanceRating.csv")
emp_df = pd.read_csv("Employee.csv")
merged_df = pr_df.merge(emp_df, how='outer', on='EmployeeID')

# Calculated number of employees with no performance data.
NullEmployees = merged_df["PerformanceID"].isnull().sum()

st.scatter_chart(data=merged_df, x='YearsSinceLastPromotion', y='Attrition', x_label='Years Since Last Promotion', y_label='Attrtion', color=None, size=None, width=None, height=None, use_container_width=True)