# Import packages

import streamlit as st
import pandas as pd
import numpy as np


df = pd.read_csv("Employee.csv")    # Created dataframe df using Employee.csv
st.write(df)                        # Ran dataframe into Streamlit web app