#CLEANING US CENSUS DATA PROJECT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn

import glob #glob allows us to cluster together several files in order to loop through them and create a dataframe from them

#glob the files together:
files = glob.glob("states*.csv")
df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
us_census = pd.concat(df_list)
print(us_census)

#columns and datatypes and head():
print(us_census.columns, us_census.dtypes)
print(us_census.head())

#Regex on the income column:
us_census.Income = us_census["Income"].str.replace("$","",regex=True)
us_census.Income = pd.to_numeric(us_census.Income)
#print(us_census.Income)

#Split the GenderPop column into men and women:
gender_split = us_census.GenderPop.str.split("_")
us_census["MalePop"] = gender_split.str.get(0)
us_census["FemalePop"] = gender_split.str.get(1)

#Convert male and female population to numeric:
us_census.MalePop = us_census["MalePop"].str.replace("M","",regex=True)
us_census.MalePop = pd.to_numeric(us_census.MalePop)
us_census.FemalePop = us_census["FemalePop"].str.replace("F","",regex=True)
us_census.FemalePop = pd.to_numeric(us_census.FemalePop)
us_census.TotalPop = pd.to_numeric(us_census.TotalPop)

#Scatter plot for women and income:
plt.scatter(us_census.FemalePop,us_census.Income)
plt.title("Females vs Incomes")
plt.xlabel("Female Population")
plt.ylabel("Income")
plt.show()
plt.clf()

#print(us_census)

#fill the nan values:
us_census.FemalePop = us_census.FemalePop.fillna(us_census.TotalPop-us_census.MalePop)
#print(us_census.FemalePop)

#drop duplicates:
us_census = us_census.drop(columns = ["Unnamed: 0"]) #this column is redundant 
print(us_census.duplicated())
us_census = us_census.drop_duplicates().reset_index(drop = True)
#print(us_census)

#Scatter plot for women and income repeated with latest data:
plt.scatter(us_census.FemalePop,us_census.Income)
plt.title("Females vs Incomes")
plt.xlabel("Female Population Millions")
plt.ylabel("Income")
x = [0, 5 * 10**6,10 * 10**6, 15 * 10**6, 20 * 10**6]
labels = [0, 5, 10, 15, 20]
plt.xticks(x, labels)
plt.show()
plt.clf()

#Histograms of race categories:
print(us_census.columns)
#convert each race column to numeric and fill the nan values:
us_census.Hispanic = us_census.Hispanic.str.replace("%","",regex=True)
us_census.Hispanic = pd.to_numeric(us_census.Hispanic)

us_census.White = us_census.White.str.replace("%","",regex=True)
us_census.White = pd.to_numeric(us_census.White)

us_census.Black = us_census.Black.str.replace("%","",regex=True)
us_census.Black = pd.to_numeric(us_census.Black)

us_census.Native = us_census.Native.str.replace("%","",regex=True)
us_census.Native = pd.to_numeric(us_census.Native)

us_census.Asian = us_census.Asian.str.replace("%","",regex=True)
us_census.Asian = pd.to_numeric(us_census.Asian)

us_census.Pacific = us_census.Pacific.str.replace("%","",regex=True)
us_census.Pacific = pd.to_numeric(us_census.Pacific)
us_census.Pacific = us_census.Pacific.fillna( 100 - us_census.Hispanic - us_census.White - us_census.Black - us_census.Native - us_census.Asian)

print(us_census)
#histograms:
plt.hist(us_census.Hispanic)
plt.xlabel("% of population within a state")
plt.ylabel("Number of states")
plt.title("Percentage of Hispanic people histogram")
plt.show()
plt.clf()

plt.hist(us_census.White)
plt.xlabel("% of population within a state")
plt.ylabel("Number of states")
plt.title("Percentage of White people histogram")
plt.show()
plt.clf()

plt.hist(us_census.Black)
plt.xlabel("% of population within a state")
plt.ylabel("Number of states")
plt.title("Percentage of Black people histogram")
plt.show()
plt.clf()

plt.hist(us_census.Native)
plt.xlabel("% of population within a state")
plt.ylabel("Number of states")
plt.title("Percentage of Native people histogram")
plt.show()
plt.clf()

plt.hist(us_census.Asian)
plt.xlabel("% of population within a state")
plt.ylabel("Number of states")
plt.title("Percentage of Asian people")
plt.show()
plt.clf()

plt.hist(us_census.Pacific)
plt.xlabel("% of population within a state")
plt.ylabel("Number of states")
plt.title("Percentage of Pacific people")
plt.show()
plt.clf()

