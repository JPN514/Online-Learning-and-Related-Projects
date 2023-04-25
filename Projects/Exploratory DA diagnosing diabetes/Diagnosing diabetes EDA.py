#Exploratory data analysis
#Diagnosing diabetes

import codecademylib3
import pandas as pd
import numpy as np

# code goes here
#load the csv file
diabetes_data = pd.read_csv("diabetes.csv")
print(diabetes_data.head()) #Has 9 columns

print(diabetes_data.BMI.count()) #Has 768 rows of data

#find number of null values by column:
print(diabetes_data.isnull().sum())

#use describe to check for missing values:
print(diabetes_data.describe(include="all")) 
#has counterintuitive values occuring throughout ie 0 for blood pressure, 846 max insulin levels, 17 max pregnacies!?!?

#we replace the instances of 0 with NaN below:
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

#check again for missing(null) values:
print(diabetes_data.isnull().sum())

#print all rows with values missing:
print(print(diabetes_data[diabetes_data.isnull().any(axis=1)])) #shows lots of missing entries in the insulin column, furthermore it appears that someone with a missing insulin measurement will also be missing another measurement.

#print data types for the df:
print(diabetes_data.dtypes)

#print unique values of the output column:
print(diabetes_data.Outcome.unique()) #contains [1,0,"O"], so we will replace the "O" with 0 below:
diabetes_data.Outcome = diabetes_data.Outcome.replace(["O"],0)
#reprint unique values after changing data type to INT:
diabetes_data.Outcome = diabetes_data.Outcome.astype(int)
print(diabetes_data.Outcome.unique()) 
