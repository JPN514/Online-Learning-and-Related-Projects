#Exploring mushrooms project::
#Charts in Python

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()
print(df.head())

#loop to run through the columns of the dataframe and create a barchart for each:
for column in columns:
  print(column)
  sns.countplot(df[column],\
  order=df[column].value_counts().index) #orders the bars by the value counts in descending order, makes bar chart more aesthetic
  plt.xticks(rotation=30, fontsize=10)    # rotates the value labels slightly so they don’t   overlap, also slightly increases font size
  plt.xlabel(column, fontsize=12)        # increases the variable label font size slightly to increase readability
  plt.title(column + " Value Counts")
  plt.show()
  plt.clf()