# STARTUP TRANSFORMATION PROJECT

# use data transforms to assess the health of a startup company 

import codecademylib3
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
#1 print head():
print(financial_data.head())

#2 split the df into its constituent columns:
month = financial_data.Month
revenue = financial_data.Revenue
expenses = financial_data.Expenses

#3,4 plot revenue:
plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()

# 5 plot monthly expenses:
plt.clf()
plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

# 6 read new expenses file and print head():
expenses_overview = pd.read_csv("expenses.csv")
print(expenses_overview.head())

# 7 split columns again:
expense_categories = expenses_overview.Expense
proportions = expenses_overview.Proportion

# 8,9 create pie chart of 7:
plt.clf()
plt.pie(proportions,labels=expense_categories)
plt.title("Expense categories")
plt.axis('Equal')
plt.tight_layout()
plt.show()

# 10 create "other" category:
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
plt.axis('Equal')
plt.tight_layout()
plt.show()

# 11 which category to focus cuts on:
expense_cut = "Salaries"

# 12 load productivity csv:
employees = pd.read_csv("employees.csv")
print(employees.head())

# 13 sort the employee data by productivity:
sorted_productivity = employees.sort_values(by=["Productivity"])
print(sorted_productivity)

# 14 get the 100 least productive employees to cut:
employees_cut = sorted_productivity.head(100)
print(employees_cut)

# 15 advice on how to transform the income and productivity data for exploration:
transformation = "Standardisation"

# 16 get commute times from employee data:
commute_times = employees["Commute Time"]
print(commute_times.head())

# 17 initial analysis on commute times:
print(commute_times.describe()) # descriptive statistics

# 18 histogram for commute times:
plt.clf()
plt.hist(commute_times)
plt.title("Employee Commute Times in Mins")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show() 
# right skewed

# 19 log transform the commute times to remove right skew: 
commute_times_log = np.log(commute_times)

# 20 create new histogram with the log-trasnformed commute times:
plt.clf()
plt.hist(commute_times_log)
plt.title("Employee Commute Times in Mins")
plt.xlabel("Commute Time")
plt.ylabel("Frequency")
plt.show() 
# slight left skew now, but more normal than before

#ISSUES WITH BELOW: 
# 21 apply standardisation on income(revenue) and productivity:
revenue_data = [revenue]
scaler = StandardScaler()
standardised_revenue = scaler.fit_transform(revenue_data)
print(standardised_revenue)
productivity_data = [sorted_productivity.Productivity]
standardised_productivity = scaler.fit_transform(productivity_data)
print(standardised_productivity)
