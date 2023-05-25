# FoodWheel project

# create a data presentation using FoodWheel's dataset

import codecademylib3
import numpy as np
# 1
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create restaurants dataframe
restaurants = pd.read_csv("restaurants.csv")

# Inspect restaurant dataframe
print(restaurants.head())

# Check number of unique cuisines
print(sorted(restaurants.cuisine.unique())) # 7 types of cuisine

# Group count by cuisine
cuisine_count = restaurants.groupby("cuisine").id.count()

# Inspect cuisine_counts dataframe
print(cuisine_count)

# Create a pie chart
plt.pie(cuisine_count,autopct="%0.1f%%", labels=sorted(restaurants.cuisine.unique()))
plt.title("Cuisine proportions")
plt.axis('equal')
plt.show()

# 2
# Create orders dataframe
orders = pd.read_csv("orders.csv")

# Inspect the orders dataframe
print(orders.head())

# Create new month column
mylambda = lambda x : x.split("-")[0]
orders["month"] = orders["date"].apply(mylambda)
# Inspect new orders dataframe
print(orders.head())

# Create average order by month dataframe
avg_order = orders.groupby("month").price.mean()
# Inspect avg_order dataframe
print(avg_order)

# Create standard deviation dataframe
std_order = orders.groupby("month").price.std()
# Inspect std_order
print(std_order)

# Create barplot
months = ["Apr","May","June","July","Aug","Sept"]
fig = plt.figure(figsize=(10,10))
plt.bar(range(len(months)),avg_order,yerr=std_order,capsize=5)
plt.title("Total Prices of Orders Per Month")
ax = plt.subplot()
ax.set_xticks(range(len(months)))
ax.set_xticklabels(months)
plt.ylabel("Total Price $")
plt.show()
plt.clf()
# 3
# Create customer amount dataframe
customer_amount = orders.groupby("customer_id").price.sum()
# Inspect customer amount
print(customer_amount)
# Create histogram
plt.hist(customer_amount, bins = 40, range = (0, 200))
plt.xlabel("Total Spent")
plt.ylabel("Number of Customers")
plt.title("Customer Spend")
plt.show()
