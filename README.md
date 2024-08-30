# Python for Data Analysis
This is my repo for all my Python work. 

This repo consist of the following
 # Project Title: Analysing Sales Data

 ### Objective
The primary objective of this project is to analyze sales data to gain insights into sales performance across various dimensions, including sales amounts, product categories, and fulfillment methods. The analysis will address specific questions related to sales transactions and provide aggregated insights.
 ### Data Preparation
   + Data Cleaning: Removed rows with missing values, particularly focusing on the 'Amount' column to ensure accurate analysis.
   + Data Exploration: Conducted initial exploration to understand data structure and types, and to identify any anomalies or missing information.
 ### Deliverables
   + Average sales by category and status (Excel file report) 
   + Total sales by shipment and fulfillment type (Excel file report) 

 ### Conclusion
This analysis provides valuable insights into the sales performance across different dimensions. The findings can be used to inform strategic decisions related to inventory management, marketing, and sales strategies. Further analysis can be conducted to explore additional dimensions or trends over time.

## Analysing Sales Data: amazonproject.py


# Project Title: E-commerce Data Analysis and Visualization

**Project Overview:**
This project involves analyzing and visualizing e-commerce data from multiple sources, including orders, payments, and customer information. The goal is to gain insights into payment patterns, customer behavior, and overall business performance.

**Data Sources:**
- Orders data (orders.xlsx)
- Payment data (order_payment.xlsx)
- Customer data (customers.xlsx)

**Data Preparation:**
1. Load data from Excel files using pandas
2. Handle missing values by filling with 'N/A' or dropping rows
3. Remove duplicate entries
4. Create subsets of data based on specific criteria (e.g., invoiced orders, credit card payments > 1000)
5. Merge datasets to create a comprehensive view of orders, payments, and customers

**Analysis and Visualization:**
1. Time-based analysis:
   - Create time-based columns (year, month, week)
   - Plot payment values over time

2. Payment analysis:
   - Scatter plot of payment values vs. installments by customer
   - Stacked bar chart of payment values by payment type and month
   - Box plot of payment value ranges by payment type

3. Combined visualization:
   - Create subplots combining box plot, stacked bar chart, and scatter plot for comprehensive view

**Key Findings:**
(Note: Specific findings would depend on the actual data analysis results)

**Recommendations:**
(Note: Recommendations would be based on the analysis findings)

**Next Steps:**
1. Perform more in-depth statistical analysis
2. Explore customer segmentation based on payment behavior
3. Investigate seasonal trends in sales and payments
4. Analyze the relationship between payment types and order values

**Technical Implementation:**
- Python libraries used: pandas, matplotlib, seaborn
- Data manipulation techniques: grouping, merging, filtering
- Visualization types: line plots, scatter plots, bar charts, box plots

This project demonstrates proficiency in data handling, analysis, and visualization using Python, providing valuable insights for e-commerce business decision-making.

## Code for E-commerce Data Analysis and Visualization: olisanalytics.py

# Project Title: LendingClub Loan Analysis and Risk Assessment

**Project Overview:**
This project involves analyzing loan data from LendingClub to predict borrower repayment likelihood and assess loan risk. The analysis includes data preprocessing, exploratory data analysis, and visualization of key loan attributes and risk factors.

**Data Sources:**
- Loan dataset (loandataset.xlsx)
- Customer data (customer_data.csv)
  
**Data Preparation:**
1. Import necessary libraries (pandas, seaborn, matplotlib)
2. Load data from Excel and CSV files
3. Merge loan and customer datasets
4. Handle missing values by filling with 'Unknown' or dropping rows
5. Remove duplicate entries
6. Create derived columns for risk assessment and FICO score categorization

**Analysis and Visualization:**
1. Loan purpose distribution:
- Bar plot of loan purposes
  
2. Debt-to-Income (DTI) analysis:
- Scatter plot and hexbin plot of DTI vs. annual income
  
3. FICO score analysis:
- Histogram of FICO score distribution
  
4. Risk assessment:
- Box plot of interest rates vs. risk levels
  
5. Combined visualization:
- Subplots combining all above visualizations for comprehensive view
  
**Key Functions and Classes:**
1. categorize_purpose(): Categorizes loan purposes into broader categories
2. assess_risk(): Determines loan risk based on DTI, delinquency, and revolving utilization
3. categorize_fico(): Categorizes FICO scores into ranges (Excellent, Very Good, Good, Fair, Poor)
4. DataAnalysis class: Calculates mean and median for specified columns

**Technical Implementation:**
Python libraries used: pandas, seaborn, matplotlib
Data manipulation techniques: merging, filtering, applying functions to columns
Visualization types: bar plots, scatter plots, hexbin plots, histograms, box plots
Use of custom functions and classes for data categorization and analysis

**Next Steps:**
- Implement machine learning models for loan repayment prediction
- Perform more in-depth statistical analysis on risk factors
- Analyze temporal trends in loan data
- Investigate correlations between various loan attributes
  
This project demonstrates proficiency in data analysis, visualization, and Python programming, providing insights into loan risk assessment and borrower characteristics for LendingClub.

## Code for LendingClub Loan Analysis and Risk Assessment: loan_analysis_script.py


# Project Title: Sales Analysis for Value Inc

**Project Overview:** This project involves analyzing sales data for Value Inc, a retail store that sells household items globally in bulk. The goal is to provide a comprehensive sales dashboard that includes insights into monthly costs, profits, and top-selling products. The data is sourced from an Excel sheet provided by the Sales Manager, who requires detailed reporting on sales metrics.

## Data Sources:

**value_inc_seasons.csv:** Contains seasonal data related to sales.
transaction2.csv: Includes transaction-level data for sales analysis.

## Data Preparation:

**Import Libraries:** Used libraries include pandas, seaborn, numpy, matplotlib, and datetime.

**Load Data:** Read the CSV files value_inc_seasons.csv and transaction2.csv into pandas DataFrames.

## Explore DataFrames:
Display the first and last few rows of the datasets.
Generate descriptive statistics for a basic understanding of data distributions and summaries.
Check data types and null values with info().

## Analysis and Calculations:

**Cost and Profit Calculations:**
Calculate CostPerTransaction, SalesPerTransaction, ProfitPerTransaction, and Markup.
Add these calculated columns to the main DataFrame for comprehensive transaction-level analysis.

**Date Manipulation:**
Combine 'Day', 'Month', and 'Year' columns into a single 'Date' column.
Convert individual date components into strings before concatenation.

**Client Data Processing:**
Split the ClientKeywords column into ClientAge, ClientType, and LengthofContract.
Clean new columns by removing unnecessary characters.
Drop the original ClientKeywords column post-split.

# Data Transformation:

**Data Cleaning:**
Convert item descriptions to lowercase for consistency.
Merge seasons data with transaction data on the 'Month' column.
Drop unnecessary columns ('Year', 'Month', 'Day') post-merging.

**Export Data:**
Save the cleaned and transformed data into a CSV file named ValueInc_Clean.csv.

**Data Manipulation and Cleaning:** Several steps involving pandas operations to transform raw data into a structured format for analysis.
Calculations: Includes profit calculations, transaction costs, and markup percentages.
Data Merging: Merges multiple datasets to provide a holistic view of sales performance.
Technical Implementation:

**Python Libraries Used:** pandas, seaborn, numpy, matplotlib, datetime.

**Data Manipulation Techniques:** Importing data, cleaning, splitting columns, creating new calculated fields, and merging datasets.
Visualization Preparation: Data is prepared for future visualization using seaborn and matplotlib.

**Next Steps:**

Develop visualizations for key sales metrics.
Create a sales dashboard to present cost, profit, and top-selling product data dynamically.
Implement monthly and seasonal trend analysis to identify sales patterns.
This project showcases the ability to preprocess and analyze sales data effectively, providing actionable insights for Value Inc's sales team.

## Code for Sales Analysis for Value Inc: valueinc_sales.py


 
