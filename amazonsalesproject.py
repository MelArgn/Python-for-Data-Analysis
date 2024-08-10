# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 16:07:40 2024

@author: argnc

Questions to answer

How many sales have they made with amounts more than 1000
How many sales have they made that belongs to category "Tops" and have a quantity of 3
What is the total sales by category
Average amount by category and status
Total sales by fulfilment and shipment type

"""

# =============================================================================
# Importing The Excel File 
# =============================================================================
import pandas as pd

# =============================================================================
# Load The Sales Data From The Excel File Into a Pandas DataFrame
# =============================================================================
sales_data = pd.read_excel('sales_data.xlsx')

# =============================================================================
# Exploring The Data
# =============================================================================

# Get a Summary of The Data After Loading The File
sales_data.info() # Can check data types

# Get a Description of The Data
sales_data.describe()

# Looking At Columns
print(sales_data.columns)

# Having a Look At The First Few Rows
print(sales_data.head())

# Checking Columns Data Types
print(sales_data.dtypes)

# =============================================================================
# Cleaning The Data
# =============================================================================

# Checking For Missing Values in Our Sales Data
sales_data.isnull()

# Checking The SUM of The NULL values
print (sales_data.isnull().sum())

# Dropping Any Rows That Has Any Missing/nan Values
sales_data_dropped = sales_data.dropna()

# Dropping Rows With Missing Amounts Based On The Amount Column
sales_data_cleaned = sales_data.dropna(subset = ['Amount'])

# Checking For Missing Values In Our Sale Data After Cleaning
print(sales_data_cleaned.isnull().sum())

# =============================================================================
# Slicing and Filtering Data
# =============================================================================

# Select a Subset of Our Data Based on The Category Column
category_data = sales_data[sales_data['Category'] == 'Top']
print(category_data)

# Select a Subset of Our Data Where Amount is > 1000
high_amount_data = sales_data[sales_data['Amount'] > 1000]
print(high_amount_data)

# Slect a Subset of Data BAsed on Multiple Conditions
filtered_data = sales_data[(sales_data['Category'] == 'Top') & (sales_data['Qty'] == 3)]
print(filtered_data)


# =============================================================================
# Aggregating Sales Data
# =============================================================================

# Total Sales by Category
category_total = sales_data.groupby('Category', as_index=False)['Amount'].sum()

# Sorting in Amount Descending Order
category_total = category_total.sort_values('Amount', ascending=False)

# Calculating The Average Amount by Category and Fulfilment
fulfilment_average = sales_data.groupby(['Category', 'Fulfilment'], as_index=False)['Amount'].mean()
fulfilment_average = fulfilment_average.sort_values('Amount', ascending=False)

# Calculating The Average Amount by Category and Status
status_average = sales_data.groupby(['Category', 'Status'], as_index=False)['Amount'].mean()
status_average = status_average.sort_values('Amount', ascending=False)

# Calculating The Total Sales by Fulfilment and Shipment Type
total_sales_shipandfulfil = sales_data.groupby(['Courier Status', 'Fulfilment'], as_index=False)['Amount'].sum()
total_sales_shipandfulfil = total_sales_shipandfulfil.sort_values('Amount', ascending=False)
# This is How to Rename a Column
total_sales_shipandfulfil.rename(columns={'Courier Status' : 'Shipment'}, inplace = True)

# =============================================================================
# Exporting The Data
# =============================================================================
 # Exporting The Status Averages First
status_average.to_excel('average_sale_by_category_and_status.xlsx', index=False)
total_sales_shipandfulfil.to_excel('total_sales_by_ship_and_fulfil.xlsx', index=False)
 # Here is How To Save The File Without The Index
status_average.to_excel('average_sale_by_category_and_status.xlsx', index=False)








































