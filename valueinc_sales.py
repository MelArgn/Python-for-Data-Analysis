# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:05:44 2024

@author: argnc


Project 1: Sales Analysis for Value Inc 

Value Inc is a retail store that sells household items all over the world by bulk. 
The Sales Manager has no sales reporting but he has a brief idea of current sales.
He also has no idea of the monthly cost, profit and top selling products. He wants a 
dashboard on this and says the data is currently stored in an excel sheet


"""

# =============================================================================
# Most Commond Data Types
# =============================================================================
# Variables

var = 'Hello world' # str

var = 39 # int

var = 2.5 # float

var = 'w3f' # str

var = ['Apple', 'Pear', 'Banana'] # list

var = ('Apple', 'Pear', 'Banana') # tuple

var = range(10) # range

var = {'name': 'Melvin', 'location': 'Hyattsville MD'} # dictionary

var = {'Apple', 'Pear', 'Banana'} # set

var = True # bool


# =============================================================================
# Step 1: Import Libraries and Import the Files
# =============================================================================

# Step 1. Import the pandas library
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

import os
os.chdir(r'C:\Users\argnc\Desktop\DataAnalytics\Python_Data_Analytics_Bootcamp\python_tableau')


# =============================================================================
# Step 2: Reading the excel files function | Creating the DataFrames
# =============================================================================

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')
data = pd.read_csv('transaction2.csv', sep=';')

# =============================================================================
# Step 3: Exploring DataFrames and Descriptive Statistics
# =============================================================================

# Display the first few rows of the dataset
seasons.head()
seasons.head(10)

data.head()
data.head(10)

# Display the last few rows of the dataset
seasons.tail()
seasons.tail(10)

data.tail()
data.tail(10)

# Describing the data (Statistics)
seasons.describe()
data.describe()

# Data information 
data.info()

# =============================================================================
# Working with Calculations
# =============================================================================

# Defining variables

CostPerItem = 11.73

SellingPricePerItem = 21.11

NumberofItemsPurchased = 6

# Mathematical operations in Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

# Profit per transaction
ProfitPerTransaction = ProfitPerItem * NumberofItemsPurchased

#Cost per transaction 
CostPerTransaction = NumberofItemsPurchased * CostPerItem

# Selling price per transaction
SellingPricePerItem = NumberofItemsPurchased * SellingPricePerItem

# =============================================================================
# Applying Calculations to the Whole Column

"""
Cost per transaction column calculation
CostPerTransaction = ProfitPerItem * NumberofItemsPurchased

"""
# =============================================================================

# Creating a variable | variable_name['column_name']
CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

# Using to comfirm the calculation is correct
CostPerItem * NumberofItemsPurchased

# Adding the CostPerTransaction column to our DataFrame to apply our calculations
data['CostPerTransaction'] = CostPerTransaction

# Adding the SellsPerTransaction column to our DataFrame to apply our calculations

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Adding the ProfitPerTransaction column to our DataFrame to apply our Calculations
"""
Profit and Markup Formula

Profit: 
    Profit = sales - cost

Markup:
    Markup = (sales - cost) / cost

"""
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']


data['Markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']


# =============================================================================
# Working with Functions
# =============================================================================

# Round() Function

roundmarkup = np.round(data['Markup'].to_numpy(), decimals=2)

# Adding the round(data['Markup'] to the column

data['Markup'] = round(data['Markup'],2)

# roundmarkup = round(data['Markup'], 2)


# =============================================================================
# Combining The Date Columns Into One (Data Fields)
# =============================================================================

date = 'Month'+'-'+'Day'+'-'+'Year'

# Changing the data type with the astype() function

day = data['Day']. astype(str)
print(day.dtype)

year = data['Year']. astype(str)
print(day.dtype)

# Combining after changing the data type

Date = data['Month']+'-'+day+'-'+year

# Adding the new date column to our DataFrame
data['Date'] = Date

# Rename the 'date' column to 'Date'
#data = data.rename(columns={'date': 'Date'})

# Step 1: Move the 'date' column to the desired position (index 2)
data.insert(2, 'Date', data.pop('Date'))

# Step 2: Drop the 'Year', 'Month', and 'Day' columns
#data = data.drop(['Year', 'Month', 'Day'], axis=1)

#data = data.drop(['date'], axis=1)

# Optional: Reset the column index if needed
data = data.reset_index(drop=True)

# Print the updated DataFrame info to verify the changes
print(data.info())


# =============================================================================
# Using iloc to View Specific Columns
# =============================================================================

data.iloc[0] # Views the row with index = 0
data.iloc[0:3] # Views the rows from index 0 to index 3
data.iloc[-5:] # Views the last 5 rows
data.head(5) # Brings the first 5 rows
data.tail(5) # Brings the last 5 rows

data.info()

# Bringing all rows in a specific column
data.iloc[:, 2]

# Bringing an specific row and a specific column
data.iloc[4,2]

# =============================================================================
# Spliting Columns | Spliting the ClientKeywords Column Into 3 Columns
# =============================================================================

# Creating a split variable_name = data.[clumn_name].str.split('seperater character' , expand = True)
split_col = data['ClientKeywords'].str.split(',' , expand=True)


# Creating new columns for the splited ClientKeywords column

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# =============================================================================
# Replacing the Unnecessary Characters From New Columns
# =============================================================================

data['ClientAge'] = data['ClientAge'].str.replace(r'[\[\]\']' , '', regex=True)

data['ClientType'] = data['ClientType'].str.replace(r'^\s*\'|\'\s*$', '', regex=True)

data['LengthofContract'] = data['LengthofContract'].str.replace(r'^[\s\'\[\]]*|[\s\'\[\]]*$', '', regex=True)

# =============================================================================
# Dropping The ClientKeywords Column
# =============================================================================

data = data.drop(['ClientKeywords'], axis=1)

# Reset the column index if needed
data = data.reset_index(drop=True)

# =============================================================================
# Changing The ItemDescription to Lower Case | lower( Function)
# =============================================================================

# Convert to lowercase and remove extra spaces
data['ItemDescription'] = data['ItemDescription'].str.lower().str.strip()

# =============================================================================
# Merging DataFrames | Joining DataFrames
# =============================================================================

# Merging files : merged_df = pd.merge(data, seasons, on ='key')
data = pd.merge(data, seasons, on ='Month')

# Drop the 'Year', 'Month', and 'Day' columns
data = data.drop(['Year', 'Month', 'Day'], axis=1)


# =============================================================================
# Exporting The DataFrame Into a CSV File
# =============================================================================

data.to_csv('ValueInc_Clean.csv', index =False)











































