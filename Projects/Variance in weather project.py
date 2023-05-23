#Variance in weather project

import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print head(), datatypes and length:
print(london_data.head())
print(london_data.dtypes)
print(len(london_data))

#temperature in celsius:
temp = london_data["TemperatureC"]

#average temperature and variance in temp in London in 2015:
average_temp = np.mean(temp)
temp_var = np.var(temp)
print(average_temp,temp_var)

#standard deviation of the temp:
temp_std = np.std(temp)
print(temp_std)

#Filter by the month column:
june = london_data[london_data["month"]==6]["TemperatureC"]
july = london_data[london_data["month"]==7]["TemperatureC"]

#mean temp in June and July:
june_mean = np.mean(june)
july_mean = np.mean(july)
print(june_mean,july_mean)

#standard deviation for both June and July:
june_std = np.std(june)
july_std = np.std(july)
print(june_std,july_std)

#Mean and standard deviation for all months:
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")