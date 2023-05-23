#Healthcare in different states project

#A project using boxplots

import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

# print head():
print(healthcare.head())

# print unique diagnosis: 
print(healthcare["DRG Definition"].unique())

# filter for only chest pain:
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

# chest pain in Alabama:
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]

# average costs of diagnoses in Alabama:
costs = alabama_chest_pain[' Average Covered Charges '].values

# boxplot of costs of chest pain diagnoses in Alabama:
plt.boxplot(costs)
plt.title("$ cost of chest pain diagnoses in Alabama")
plt.show()
plt.clf()

# unique states in chest_pain df: 
states = chest_pain["Provider State"].unique()
print(states)

# create dataframe for each individual state using loop:
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

# boxplot for all 50 states using the datasets list above: 
plt.figure(figsize=(20,6))
plt.boxplot(datasets,labels=states)
plt.title("Cost in $ of chest pain diagnoses by state")
plt.show()


