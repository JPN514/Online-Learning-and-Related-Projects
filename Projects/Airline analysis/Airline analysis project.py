#Airline analysis project 
#charts and graphs in Python

#Took ages to compile online !!!

import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1, max and min, mean coach prices 
coach_max = flight.coach_price.max()
coach_min = flight.coach_price.min()
coach_mean = flight.coach_price.mean()
print(coach_max,coach_min,coach_mean)
#histogram of prices:
plt.hist(flight.coach_price)
plt.title("Coach prices")
plt.xlabel("Cost of caoch ticket")
plt.show()
plt.close()
## Task 2, coach prices for 8 hour flights
flights_8 = flight[flight["hours"] == 8]
plt.hist(flights_8.coach_price)
plt.title("Coach price for 8 hour flights")
plt.xlabel("Cost of coach ticket")
plt.show()
plt.close()
## Task 3, histogram of flight delays, shows 10 minute delays are prevalent
shorter_delays = flight[flight.delay < 100] 
plt.hist(shorter_delays.delay)
plt.title("Flight delays")
plt.xlabel("Delay in minutes")
plt.show()
plt.close()


## Task 4, relationship between coach prices and first class prices, using scatter plot
#plt.scatter(flight.coach_price,flight.firstclass_price)
#plt.title("First class price vs coach price")
#plt.show()
#plt.close()
#scatter is very difficult to look at so we use an alternative:
#sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight, line_kws={'color': 'black'}, lowess=True)
#plt.title("First class price vs coach price")
#plt.show()


## Task 5,relationship between coach price and other features such as inflight meal, inflight entertainment, inflight wifi etc:
inflightmeal = flight[flight.inflight_meal == "Yes"]
inflight_ent = flight[flight.inflight_entertainment == "Yes"]
wifi = flight[flight.inflight_wifi == "Yes"]

plt.hist(inflightmeal.coach_price,alpha=0.4)
plt.title("Cost of coach ticket on flights with meal")
plt.xlabel("Coach price")
plt.show()
plt.close()

plt.hist(inflight_ent.coach_price,alpha=0.4)
plt.title("Cost of coach ticket on flights with entertainment")
plt.xlabel("Coach price")
plt.show()
plt.close()

plt.hist(wifi.coach_price,alpha=0.4)
plt.title("Coach cost for flights with wifi")
plt.xlabel("Coach price")
plt.show()
plt.close()

## Task 6, number of passengers and length of flights:
plt.scatter(flight.passengers,flight.hours)
plt.title("Passengers vs Hours")
plt.xlabel("Passengers")
plt.ylabel("Duration of Flight")
plt.show()
plt.close()

## Task 7


## Task 8
