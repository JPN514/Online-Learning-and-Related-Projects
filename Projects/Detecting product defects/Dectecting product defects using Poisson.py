#Dectecting product defects using Poisson distribution:

import scipy.stats as stats
import numpy as np

### Task Group 1 ###
## Task 1: 
lam = 9 #our lambda value
## Task 2:
print("Exactly 9 defects: {} ".format(stats.poisson.pmf(lam,lam))) #exactly 9 defects on a given day
## Task 3:
print(stats.poisson.cdf(4,lam)) #4 or fewer defects
## Task 4:
print(1 - stats.poisson.cdf(9,lam)) #more than 9 defects

### Task Group 2 ###
## Task 5:
year_defects = stats.poisson.rvs(9,size=365) #poisson of defects across a whole year
## Task 6:
print(year_defects[0:20]) #first 20 projected days
## Task 7:
print(7*365) #total defects across whole year given 7 expected defects per day
## Task 8:
total_defects = sum(year_defects)
print(total_defects) #projected defects given lambda=9 from year_defects
## Task 9:
print(np.mean(year_defects)) #average defects per day
## Task 10:
print(max(year_defects)) #max defects on a single day across the year
## Task 11:
print(1 - stats.poisson.cdf(17,7)) #prob of observing 18 or more defects

### Extra Bonus ###
# Task 12
print(stats.poisson.ppf(0.9,7)) #number of defects per day that puts us in 90th percentile of Poisson(7), here 10.0 
# Task 13
print(sum(year_defects >= 10.0)/len(year_defects)) #roughly 40% of days projected to be in 90th percentile, given lambda of 7