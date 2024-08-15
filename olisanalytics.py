# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:03:44 2024

@author: argnc
"""
# =============================================================================
# Setting The Working Directory in Python
# =============================================================================
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
os.chdir(r'C:\Users\argnc\Desktop\Data Science Analyst Classes\Python and Tableau Data Bootcamp\Data\Ecommerce Orders Project')

# Check the current working directory
print(os.getcwd())

# =============================================================================
# Step 1: Loading the excel files
# =============================================================================

# Loading the orders data
orders_data = pd.read_excel('orders.xlsx')

# Loading the payments data
payments_data = pd.read_excel('order_payment.xlsx')

# Loading the customers data
# (CSV Files)You can also run pd.read_csv('File Name')
customers_data = pd.read_excel('customers.xlsx')

# =============================================================================
# Step 2: Describing the data
# =============================================================================
orders_data.info()
payments_data.info()
customers_data.info()

# =============================================================================
# Handling missing data values in Python
# =============================================================================

# Step 3: Checking for missing data in the orders dataset
orders_data.isnull().sum()
# Checking for missing data in the payments dataset
payments_data.isnull().sum()
# Checking for missing data in the customers dataset
customers_data.isnull().sum()

# =============================================================================
# Step 4: Replacing the NULL values in our dataset
# =============================================================================
# Filling in the missing NULL values in the orders dataset with default values
orders_data2 = orders_data.fillna('N/A')
# Step 5: Checking for NULL values in orders_data2 after replaced values
orders_data2.isnull().sum()

# Step 6: Dropping the 2 NULL values in the payments dataset
payments_data = payments_data.dropna()
# Step 7: Checking for NULL values in payments_data after removing the NULL values
payments_data.isnull().sum()


# =============================================================================
# Step 8: Checking for duplicate data & Removing the duplicate data
# =============================================================================
# Step 9: Checking for duplicate data in our orders data
orders_data.duplicated().sum()
# Step 10: Removing the duplicate data in the orders_data
orders_data = orders_data.drop_duplicates()
# Step 10: Checking to make sure there are no duplicats in the orders_data
orders_data.duplicated().sum()

# Step 11: Checking for duplicate data in our payments data
payments_data.duplicated().sum()
# Step 12: Removing the duplicate data in our payments_data
payments_data = payments_data.drop_duplicates()
# Step 13: Checking to make sure there are no duplicates in the payments_data
payments_data.duplicated().sum()

# Step 14: Checking for duplicate data in our customers_ data
customers_data.duplicated().sum()

# =============================================================================
# Step 15: Filtering data on Python
# =============================================================================
#  Step 16: Select a subset of the orders data based on the order_status
# Creating a DataFrame for orders_status that are being invoiced.
invoiced_orders_data = orders_data[orders_data['order_status'] == 'invoiced']
# Resetting the order_status index
invoiced_orders_data = invoiced_orders_data.reset_index(drop=True)

# Creating a subset of our payments_data where payment_type is via credit_card
# with a payment > 1000
credit_card_payments_data = payments_data[
    (payments_data['payment_type'] =='credit_card') &
    (payments_data['payment_value'] > 1000)
    ]

# Sorting the payment_value in descending order
credit_card_payments_data = credit_card_payments_data.sort_values('payment_value', ascending=False)

# Resetting the payments_data index
credit_card_payments_data = credit_card_payments_data.reset_index(drop=True)

# Creating a subset of our customers_data where state = sp
customers_state_data = customers_data[customers_data['customer_state'] == 'SP']

# Resetting the customer_state_data index
customers_state_data = customers_state_data.reset_index(drop=True)


# =============================================================================
# Merging and Joining Different DataFrames
# =============================================================================

# Merging orders_data with payments_data on order_id column
merged_data = pd.merge(orders_data, payments_data, on='order_id')

# Joining the merged_data with our customer_data on the customer_id column
joined_data = pd.merge(merged_data, customers_data, on='customer_id')

# =============================================================================
# Creating Data Visualizations
# =============================================================================
# Step 1: Create a column called year_month from order_purchase_timestamp 
joined_data['year_month'] = joined_data['order_purchase_timestamp'].dt.to_period('M')
joined_data['year_week'] = joined_data['order_purchase_timestamp'].dt.to_period('W')
joined_data['year'] = joined_data['order_purchase_timestamp'].dt.to_period('Y')

# Creating a table to group our data
grouped_data = joined_data.groupby('year_month')['payment_value'].sum()
# Resetting the payments_data index
grouped_data = grouped_data.reset_index()

# Converting year_month from Dtype period(M) to string
grouped_data['year_month'] = grouped_data['year_month'].astype(str)

# Creating and running a plot
plt.plot(grouped_data['year_month'], grouped_data['payment_value'], color='blue', marker='o')
# Formating the y axis from expenatial to the whole number
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
# Creating a lable and cleaning our plot.
plt.xlabel('Year and Month', color='blue')
# Rotating labels because they are on-top of each other
plt.xticks(rotation = 90, fontsize=8)
# Optionally, add other plot elements
plt.ylabel('Payment Value', color='blue')   # Label for the y-axis
plt.title('Payments Over Time', color='blue')  # Title for the plot
plt.yticks(fontsize=8)
plt.tight_layout()  # Adjusts the layout so plots don't overlap

# =============================================================================
# Creating a Scatter Plot to mesure two mesureble fields 
# =============================================================================

# Creating DataFrame
scatter_df = joined_data.groupby('customer_unique_id').agg({'payment_value' : 'sum', 'payment_installments' : 'sum'})

plt.scatter(scatter_df['payment_value'], scatter_df['payment_installments'])                      
plt.xlabel('Payment Value')
plt.ylabel('Payment Installments')
plt.title('Payment Value vs Installments by Customer')
plt.show()
plt.tight_layout()  # Adjusts the layout so plots don't overlap
# =============================================================================
# Using Seaborn to create a scatter plot
# =============================================================================

sns.set_theme(style='darkgrid') # whitegrid, darkgrid, dark and white
sns.scatterplot(data=scatter_df, x='payment_value', y="payment_installments")
plt.xlabel('Payment Value')
plt.ylabel('Payment Installments')
plt.title('Payment Value vs Installments by Customer')
plt.show()
plt.tight_layout()  # Adjusts the layout so plots don't overlap
# =============================================================================
# Creating a Stacked Bar Chart
# =============================================================================

# Visulyzing payment value by payment type for each month of the year
bar_chart_df = joined_data.groupby(['payment_type', 'year_month'])['payment_value'].sum()
bar_chart_df = bar_chart_df.reset_index()

# Creating a pivot DataFrame
pivot_data = bar_chart_df.pivot(index='year_month', columns='payment_type', values='payment_value')

# Stacked Bar Chart
pivot_data.plot(kind='bar', stacked='True')
plt.ticklabel_format(useOffset=False, style='plain', axis='y') # Getting ridoff the scientific notation
plt.xlabel('Month of Payment')
plt.ylabel('Payment Value')
plt.title('Payments per Payment Type by Month')
plt.show()
plt.tight_layout()  # Adjusts the layout so plots don't overlap
# =============================================================================
# Creating Boxplots on Python
# =============================================================================
# Creating a ranges of pyments values by credit card
payment_values = joined_data['payment_value']
payment_types = joined_data['payment_type']

# Creating a seperate Box Plot for each payment type
plt.boxplot([payment_values[payment_types == 'credit_card'],
             payment_values[payment_types == 'boleto'],
             payment_values[payment_types == 'voucher'],
             payment_values[payment_types == 'debit_card']],
            labels=['Credit Card', 'Boleto', 'Voucher', 'Debit Card']
            )
# Setting labels and titles
plt.xlabel('Payment Type')
plt.ylabel('Payment Value')
plt.title('Payment Value Ranges by Payment Type')
plt.show()
plt.tight_layout()  # Adjusts the layout so plots don't overlap
# =============================================================================
# Creating Subplots in Python (Combining all of the plots into one plot)
# =============================================================================
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(25, 30))

# ax1 is the boxplot
# Creating a seperate Box Plot for each payment type
ax1.boxplot([payment_values[payment_types == 'credit_card'],
             payment_values[payment_types == 'boleto'],
             payment_values[payment_types == 'voucher'],
             payment_values[payment_types == 'debit_card']],
            labels=['Credit Card', 'Boleto', 'Voucher', 'Debit Card']
            )
# Setting labels and titles
ax1.set_xlabel('Payment Type')
ax1.set_ylabel('Payment Value')
ax1.set_title('Payment Value Ranges by Payment Type')


# ax2 is the stacked bar chart
# Stacked Bar Chart
pivot_data.plot(kind='bar', stacked='True', ax=ax2)
ax2.ticklabel_format(useOffset=False, style='plain', axis='y') # Getting ridoff the scientific notation

#Setting labels and titles
ax2.set_xlabel('Month of Payment')
ax2.set_ylabel('Payment Value')
ax2.set_title('Payments per Payment Type by Month')

#ax3 is the scatterplot
ax3.scatter(scatter_df['payment_value'], scatter_df['payment_installments'], color='lightblue') 

#Setting labels and titles   
sns.set_theme(style='darkgrid') # whitegrid, darkgrid, dark and white
sns.scatterplot(data=scatter_df, x='payment_value', y="payment_installments")
ax3.set_xlabel('Payment Value')
ax3.set_ylabel('Payment Installments')
ax3.set_title('Payment Value vs Installments by Customer')


"""                  
ax3.set_xlabel('Payment Value')
ax3.set_ylabel('Payment Installments')
ax3.set_title('Payment Value vs Installments by Customer')
"""

# Need to save the file before it's shown
plt.savefig('my_plot.png', format='png', dpi=1200)

# Display the plots
plt.tight_layout()  # Adjusts the layout so plots don't overlap
plt.show()
