# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:43:24 2024

@author: argnc

Project 4: LendingClub

Overview:
As a data analyst for LendingClub you are tasked with the goal of building a simple model to predict
whether or not a borrower will pay back their loan in full. This prediction will be based on various details
about the loan and the borrower such as the purpose of the loan, interest rate, FICO score, debt-toincome ratio, 
and other factors. You’re also responsible for developing some visualizations.

Datasets:
There are two data sets availabel

loandataset.xlsx
customer_data.csv


credit.policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.
purpose: The purpose of the loan (takes values "credit_card", "debt_consolidation", "educational", "major_purchase", "small_business",
and "all_other").

int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers judged by
LendingClub.com to be more risky are assigned higher interest rates.

installment: The monthly installments owed by the borrower if the loan is funded.

log.annual.inc: The natural log of the self-reported annual income of the borrower.

dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income).

fico: The FICO credit score of the borrower (see next slide)

days.with.cr.line: The number of days the borrower has had a credit line.

revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).

revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit
available).
    
inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months.

delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years.

pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments).

There's more than one credit scoring model available and more than one range of scores. However, most credit
score ranges are similar to the following:

800 to 850: ExcellentIndividuals in this range are considered to be low-risk borrowers. They may have an
easier time securing a loan than borrowers with lower scores.

740 to 799: Very goodIndividuals in this range have demonstrated a history of positive credit behavior and
may have an easier time being approved for additional credit.

670 to 739: GoodLenders generally view those with credit scores of 670 and up as acceptable or lower-risk
borrowers.

580 to 669: FairIndividuals in this category are often considered “subprime” borrowers. Lenders may consider
them higher-risk, and they may have trouble qualifying for new credit.

300 to 579: PoorIndividuals in this range often have difficulty being approved for new credit. If you find
yourself in the poor category, it's likely you'll need to take steps to improve your credit scores before you can
secure any new credit


"""

# =============================================================================
# Step 1: Import Libraries and Import the Files
# =============================================================================

# Step 1. Import the pandas library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import os
os.chdir(r'C:/Users/argnc/Desktop/DataAnalytics/Python_Data_Analytics_Bootcamp/Data/Loan Analysis Project')

# =============================================================================
# Step 2: Reading the excel files function | Creating the DataFrames
# =============================================================================
loan_data = pd.read_excel('loandataset.xlsx')
customer_data = pd.read_csv('customer_data.csv', sep=';')

# =============================================================================
# Step 3: Exploring DataFrames and Descriptive Statistics
# =============================================================================

# Display the first few rows of the dataset
loan_data.head()
loan_data.head(10)

customer_data.head()
customer_data.head(10)

# Display the last few rows of the dataset
loan_data.tail()
loan_data.tail(10)

customer_data.tail()
customer_data.tail(10)

# Describing the data (Statistics)
loan_data.describe()
customer_data.describe()

# =============================================================================
# Step 4: Performing Data Validation Check and Checking the non-NULL
# =============================================================================
loan_data.info()
customer_data.info()

# =============================================================================
# Step 5: Checking for the NULL count per column
# =============================================================================
null_count = loan_data.isnull().sum()
null_count = customer_data.isnull().sum()

# =============================================================================
# Step 6:Checking for duplicated rows
# =============================================================================

duplicated_rows = loan_data.duplicated().sum()
print(duplicated_rows)

duplicated_rows = customer_data.duplicated().sum()
print(duplicated_rows)

# =============================================================================
# Step 7: Joining the DataFrames
# =============================================================================
# Using left and right to merge DataFrames when the columns names are different 
complete_data = pd.merge(loan_data, customer_data, left_on='customerid', right_on='id')

# =============================================================================
# Step 8: Cleaning Analysis Steps | Checking For Missing Data
# =============================================================================
complete_data.isnull().sum()

# =============================================================================
# Step 9: Deleting Rows with Missing Data (na) (If Applicable)
# =============================================================================
complete_data = complete_data.dropna()

# =============================================================================
# Step 10: Replacing the Missing Values with 'Unknown' to Keep All Rows in the Model
# =============================================================================
complete_data['city'].fillna('Unknown', inplace=True)
complete_data['country'].fillna('Unknown', inplace=True)

complete_data.isnull().sum()

# =============================================================================
# Step 11: Checking for Duplicated Data
# =============================================================================
complete_data.duplicated()
complete_data.duplicated().sum()
    
# Getting rid of duplicated rows (If any)
complete_data = complete_data.drop_duplicates()


# =============================================================================
# Functions in Python

"""
In Python, a function is a block of reusable code that performs a specific task. 
It can take inputs (arguments), process them, and return an output. 
Functions help organize code, reduce repetition, 
and make programs easier to understand and maintain.

Structor:
    def fuction_name(parameter1, parameter2)
    - operation that needs to be done
    return result

def greet(name):
    This function greets the person whose name is passed as a parameter.
    return f"Hello, {name}!"

"""

# =============================================================================

# Creating the function
def add_numbers(number1, number2):
    sum = number1 + number2
    return sum

# Calling the function
result = add_numbers(10, 15)
print(result)

# =============================================================================
# Creating a Function in the Loan Dataset
# =============================================================================

# Defining a function to categorize purpose into a broader categories

def categorize_purpose(purpose):
    if purpose in['credit_card', 'debt_consolidation']:
        return 'Debt Management'
    elif purpose in['educational']:
        return 'Education'
    elif purpose in['small_business']:
        return 'Business/Investment'
    else:
        return 'Other'

categorize_purpose('credit_card')

categorize_purpose('home_improvement')

# Applying the categorize_purpose function to the purpose column in the loan_data DataFrame

complete_data['purpose'].apply(categorize_purpose)

# Once the categorize_purpose function is applied. I'd add the new column to the DataFrame

complete_data['purpose_category'] = complete_data['purpose'].apply(categorize_purpose)

# =============================================================================
# Creating a Conditional Statement Function in Python

"""
Conditional statements in Python allow you to execute different blocks of code based on certain conditions. 
The most common conditional statements are if, elif, and else, which let you test conditions and 
run specific code depending on whether the condition is true or false.

"""
# =============================================================================

def check_number(number):
    if number > 0:
        return 'Positive'
    elif number <0:
        return 'Negative'
    else:
        return 'Zero'
    
result = check_number(-10)
print(result)

result = check_number(3)
print(result)

result = check_number(0)
print(result)


# =============================================================================
# Practical Application of Functions and Conditions in Our DataFrame

"""
Selecting the DTI > than 20, the delinq.2years > 2 and the revol.util
> 60. The borrower is high risk

"""
# =============================================================================

# Creating a new function based on criteria

def asses_risk(row):
    if row['dti'] > 20 and row['delinq.2yrs'] > 2 and row['revol.util'] > 60:
        return 'High Risk'
    else:
        return 'Low Risk'

complete_data['risk'] = complete_data.apply(asses_risk, axis=1)

# =============================================================================
#  Creating a Function to Categorize the FICO Scores BAsed on Their Given Ranges
# =============================================================================

def categorize_fico(fico_score):
    if fico_score >= 800 and fico_score <= 850:
        return 'Excellent'
    if fico_score >= 740 and fico_score < 800:
        return 'Very Good'
    if fico_score >= 670 and fico_score < 740:
        return 'Good'
    if fico_score >= 580 and fico_score < 670:
        return 'Fair'
    else:
        return 'Poor'
    
complete_data['fico_category'] = complete_data['fico'].apply(categorize_fico)

# =============================================================================
# Working with Conditional Statements and Averages in Functions

"""
Creating a function with customers with higher than average inquiries in 
the last 6 months. Also, highest than the average derogatory public record

"""
# =============================================================================

# Identify customers with more than the average inquiries and derogatory records

def identify_high_inq_derog(row):
    average_inq = complete_data['inq.last.6mths'].mean()
    average_derog = complete_data['pub.rec'].mean()
    
    if row['inq.last.6mths'] > average_inq and row['pub.rec'] > average_derog:
        return True
    else:
        return False
    
complete_data['high_inquiries_and_public_records'] = complete_data.apply(identify_high_inq_derog, axis=1)


# =============================================================================
# Classes in Python

"""
A class in Python is a blueprint for creating objects. It encapsulates data and
 functions that operate on that data into a single unit. 
 Classes provide a means of bundling data and functionality together, 
 allowing for the creation of reusable and organized code through object-oriented programming.

"""
# =============================================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def adult(self):
        if self.age >= 18:
            return "I'm an adult."
        else:
            return "I'm not an adult."

# Creating an instance of a class

person1 = Person("Margarita", 18)
person1.greet()
person1.adult()


# =============================================================================
# Creating a Class

"""
Creating a class to determine the mean and the median of an expecific column in our
DataFrame

"""
# =============================================================================

# Creating a data analysis class to calculate summary statistics

class DataAnalysis:
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
    
    def calculate_mean(self):
        return self.df[self.column_name].mean()
    
    def calculate_median(self):
        return self.df[self.column_name].median()

analysis = DataAnalysis(complete_data, 'fico')

mean_fico = analysis.calculate_mean() # Calling the function within the class

median_fico = analysis.calculate_median() # Calling the function within the class


# =============================================================================
# Data Visualizations in Python | Loan purpose distribution bar plot
# =============================================================================

# Set the style with seaborn (darkgrid, whitegrid, dark, white)

sns.set_style('darkgrid')

# Seaborn palettes: deep, pastel, dark, muted, bright, colorblind

plt.figure(figsize=(20,10))
sns.countplot(x='purpose', data=complete_data, palette='pastel')
plt.title('Loan Purpose Distribution', fontsize=20)
plt.xlabel('Purpose of Loans', fontsize=16)
plt.ylabel('Number of Loans', fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Set background color to translucent black
#plt.gca().set_facecolor((0, 0, 0, 0.6))  # RGB + Alpha (transparency)

# Improve the layout
plt.tight_layout()

plt.show()


# =============================================================================
# Data Visualizations in Python | Debt Income Ratio to Income
# =============================================================================

plt.figure(figsize=(20,10))
sns.scatterplot(x = 'log.annual.inc', y = 'dti', data = complete_data)
plt.title('Debt Income Ratio to Income', fontsize = 20)
plt.xlabel('Annual Income', fontsize = 16)
plt.ylabel('DTI', fontsize = 16)


# Improve the layout
plt.tight_layout()

plt.show()



plt.figure(figsize=(20,10))
plt.hexbin(x=complete_data['log.annual.inc'], y=complete_data['dti'], gridsize=50, cmap='Blues')
plt.title('Debt Income Ratio to Income', fontsize=20)
plt.xlabel('Annual Income', fontsize=16)
plt.ylabel('DTI', fontsize=16)
plt.colorbar(label='Count')

# Improve the layout
plt.tight_layout()

plt.show()


# =============================================================================
# Data Visualizations in Python | FICO Scores Distribution
# =============================================================================

plt.figure(figsize=(20,10))
sns.histplot(complete_data['fico'], bins=30, kde = True, color=sns.color_palette('pastel')[0])
plt.title('FICO Scores Distribution', fontsize=20)
plt.xlabel('FICO Score', fontsize=16)  # X-axis label
plt.ylabel('Number of Borrowers', fontsize=16)  # Y-axis label

# Improve the layout
plt.tight_layout()

plt.show()


# =============================================================================
# Data Visualizations in Python | Risk Category vs Interest Rates
# =============================================================================

plt.figure(figsize=(20,10))
sns.boxplot(x = 'risk', y = 'int.rate', data = complete_data, palette='pastel')
plt.title('Interest Rates vs Risk')
plt.xlabel('Risk Level', fontsize=16)  # X-axis label
plt.ylabel('Interest Rate (%)', fontsize=16)  # Y-axis label

# Improve the layout
plt.tight_layout()

plt.show()


# =============================================================================
# Data Visualizations in Python | Subplots in Python
# =============================================================================


# Set the style with seaborn (darkgrid, whitegrid, dark, white)
sns.set_style('darkgrid')

# Create a figure and an array of subplots
fig, axs = plt.subplots(3, 2, figsize=(24, 18))  # 3 rows, 2 columns

# Adjust spacing between subplots
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# 1st plot: Loan purpose distribution bar plot
sns.countplot(x='purpose', data=complete_data, palette='pastel', ax=axs[0, 0])
axs[0, 0].set_title('Loan Purpose Distribution', fontsize=20)
axs[0, 0].set_xlabel('Purpose of Loans', fontsize=16)
axs[0, 0].set_ylabel('Number of Loans', fontsize=16)
axs[0, 0].tick_params(axis='x', rotation=45)

# 2nd plot: Debt Income Ratio to Income (scatter plot)
sns.scatterplot(x='log.annual.inc', y='dti', data=complete_data, ax=axs[0, 1], color=sns.color_palette('pastel')[1])
axs[0, 1].set_title('Debt Income Ratio to Income', fontsize=20)
axs[0, 1].set_xlabel('Annual Income', fontsize=16)
axs[0, 1].set_ylabel('DTI', fontsize=16)

# 3rd plot: Debt Income Ratio to Income (hexbin plot)
axs[1, 0].hexbin(x=complete_data['log.annual.inc'], y=complete_data['dti'], gridsize=50, cmap='Blues')
axs[1, 0].set_title('Debt Income Ratio to Income', fontsize=20)
axs[1, 0].set_xlabel('Annual Income', fontsize=16)
axs[1, 0].set_ylabel('DTI', fontsize=16)
fig.colorbar(axs[1, 0].collections[0], ax=axs[1, 0], label='Count')

# 4th plot: FICO Scores Distribution
sns.histplot(complete_data['fico'], bins=30, kde=True, color=sns.color_palette('pastel')[0], ax=axs[1, 1])
axs[1, 1].set_title('FICO Scores Distribution', fontsize=20)
axs[1, 1].set_xlabel('FICO Score', fontsize=16)
axs[1, 1].set_ylabel('Number of Borrowers', fontsize=16)

# 5th plot: Risk Category vs Interest Rates
sns.boxplot(x='risk', y='int.rate', data=complete_data, palette='pastel', ax=axs[2, 0])
axs[2, 0].set_title('Interest Rates vs Risk', fontsize=20)
axs[2, 0].set_xlabel('Risk Level', fontsize=16)
axs[2, 0].set_ylabel('Interest Rate (%)', fontsize=16)

# If you have only 5 plots, you can remove the 6th subplot or leave it blank
fig.delaxes(axs[2, 1])  # Remove the unused subplot

# Improve the layout for better visualization
plt.tight_layout()

plt.show()



































































