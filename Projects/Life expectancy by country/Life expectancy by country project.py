#Life expectancy by country
#Using quantiles, iqr.

import codecademylib3_seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_data.csv")

#Print first 5 rows:
print(data.head())

#Isolate the life_expectancy column:
life_expectancy = data["Life Expectancy"]

#Find the quartiles:
life_expectancy_quartiles = np.quantile(life_expectancy,[0.25,0.5,0.75])
print(life_expectancy_quartiles)

#plot a histogram:
plt.hist(life_expectancy)
plt.xlabel("Life Expectancy (Years)")
plt.ylabel("Frequency")
plt.title("Histogram of Life Expectancy")
plt.show()
plt.clf()

#70 years life expectancy falls in the second quartile

#Isolate the GDP column:
gdp = data.GDP

#Median of GDP:
median_gdp = np.median(gdp)
print(median_gdp)

#All countries below median GDP:
low_gdp = data[data['GDP'] <= median_gdp]
#All countries above median GDP:
high_gdp = data[data['GDP'] >= median_gdp]

#Quartiles life expectancy for low gdp countries:
low_gdp_life = low_gdp["Life Expectancy"]
low_gdp_quartiles = np.quantile(low_gdp_life,[0.25,0.5,0.75])
print(low_gdp_quartiles)

#Quartiles life expectancy for high gdp countries:
high_gdp_life = high_gdp["Life Expectancy"]
high_gdp_quartiles = np.quantile(high_gdp_life,[0.25,0.5,0.75])
print(high_gdp_quartiles)

#Plot the histograms for low_gdp and high_gdp life expectancy:
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()