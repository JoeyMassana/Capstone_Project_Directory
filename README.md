## Analysis of Employee Attrition & Performance
# Overview
This project provides a comprehensive analysis of employee attrition and performance using a dataset sourced from Kaggle. The analysis explores various factors impacting employee satisfaction and retention, including job satisfaction, training opportunities, and years since the last promotion. The findings are visualized through interactive dashboards, enabling stakeholders to assess satisfaction levels among employees who have left the organization versus those who have remained.

# Features
- Interactive Dashboards: Visualize and explore employee satisfaction ratings and training opportunities.
- Data Visualization: Includes histograms and bar plots for a clear understanding of employee performance metrics.
- Data Analysis: Data transformation. Merges and reshapes multiple datasets to provide a holistic view of employee attrition and satisfaction levels.

# Requirements
To run this application, ensure you have the following Python packages installed:
- anaconda v3.12.4
- streamlit v1.32.0
- pandas
- seaborn
- matplotlib
You can install these packages using pip install v24:
pip install streamlit pandas seaborn matplotlib

# Dataset
This project utilizes three CSV files:
- PerformanceRating.csv: Contains performance ratings of employees.
- Employee.csv: Contains demographic and employment data.
- RatingLevel.csv: Contains mapping of satisfaction ratings.
Make sure to place these CSV files in the same directory as your main script.

# Usage
1. Clone the repository or download the code files.
2. Navigate to the directory containing the main .py script and the CSV files.
3. Run the Streamlit app using the following command: "streamlit run app.py"
4. Open the provided local URL in your web browser to interact with the analysis.

# Key Features in the App
- Employee Data Overview: Displays a comprehensive DataFrame containing merged employee data.
- Satisfaction Ratings Visualization: Allows users to select a satisfaction rating and visualize histograms for employees who have left versus those who have stayed.
- Training Opportunities Comparison: Bar plot comparing training opportunities offered and taken by employees in different departments.
- Years Since Last Promotion Analysis: Histogram illustrating the distribution of years since the last promotion for employees who left or stayed.

# Conclusions
The application includes a section for conclusions where key findings and insights can be summarized. This section can be modified to include more detailed interpretations based on the analysis results. Initial data exploration was conducted in Notebook-1.5.ipynb.

# Future Work
Potential future enhancements for this project may include:
- Adding more advanced statistical analyses.
- Incorporating machine learning models for predictive analytics.
- Expanding visualizations with additional data points.

# Acknowledgements
Thanks to the Kaggle community for providing the dataset and to the developers of the libraries used in this project.
- Abdallah, M. E. (2021). HR analytics: Employee attrition and performance [Data set]. Kaggle. https://www.kaggle.com/datasets/mahmoudemadabdallah/hr-analytics-employee-attrition-and-performance
Feel free to reach out if you have any questions or feedback regarding this project!