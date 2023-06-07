#File for lessons within the Advanced Exploratory Data Analysis course.


#VARIANCE AND STANDARD DEVIATION LESSON::::::

import numpy as np
import matplotlib.pyplot as plt
#import codecademylib3_seaborn

teacher_one_grades = [83.42, 88.04, 82.12, 85.02, 82.52, 87.47, 84.69, 85.18, 86.29, 85.53, 81.29, 82.54, 83.47, 83.91, 86.83, 88.5, 84.95, 83.79, 84.74, 84.03, 87.62, 81.15, 83.45, 80.24, 82.76, 83.98, 84.95, 83.37, 84.89, 87.29]
teacher_two_grades = [85.15, 95.64, 84.73, 71.46, 95.99, 81.61, 86.55, 79.81, 77.06, 92.86, 83.67, 73.63, 90.12, 80.64, 78.46, 76.86, 104.4, 88.53, 74.62, 91.27, 76.53, 94.37, 84.74, 81.84, 97.69, 70.77, 84.44, 88.06, 91.62, 65.82]

print("Teacher One mean: " + str(np.mean(teacher_one_grades)))
print("Teacher Two mean: " + str(np.mean(teacher_two_grades)))

plt.subplot(211)
plt.title("Teacher One Grades")
plt.xlabel("Grades")
plt.hist(teacher_one_grades)
plt.xlim(65, 105)

plt.subplot(212)
plt.title("Teacher Two Grades")
plt.xlabel("Grades")
plt.hist(teacher_two_grades, bins = 20)
plt.xlim(65, 105)

plt.tight_layout()
plt.show()

#difference from the mean
grades = [88, 82, 85, 84, 90]
mean = np.mean(grades)

difference_one = (88 - mean) **2
difference_two = (82 - mean) **2
difference_three = (85 - mean) **2
difference_four = (84 - mean) **2
difference_five = (90 - mean) **2

# IGNORE CODE BELOW HERE
print("The mean of the data set is " + str(mean) + "\n")
print("The first student is " +str(round(difference_one, 2)) + " percentage points away from the mean.")
print("The second student is " +str(round(difference_two, 2)) + " percentage points away from the mean.")
print("The third student is " +str(round(difference_three, 2)) + " percentage points away from the mean.")
print("The fourth student is " +str(round(difference_four, 2)) + " percentage points away from the mean.")
print("The fifth student is " +str(round(difference_five, 2)) + " percentage points away from the mean.")

#Part 1: Sum the differences
difference_sum = difference_one + difference_two + difference_three + difference_four + difference_five

#Part 2: Average the differences
average_difference = difference_sum / 5

#IGNORE CODE BELOW HERE
print("The sum of the differences is " + str(format(difference_sum, "f")))
print("The average difference is " + str(format(average_difference, "f")))

teacher_one_variance = np.var(teacher_one_grades)
teacher_two_variance = np.var(teacher_two_grades)
#IGNORE THE CODE BELOW HERE
plt.hist(teacher_one_grades, alpha = 0.75, label = "Teacher 1 Scores", bins = 7)
plt.hist(teacher_two_grades, alpha = 0.5, label = "Teacher 2 Scores", bins = 30)
plt.title("Student test grades in two different classes")
plt.xlabel("Grades")
plt.legend()
plt.show()

print("The mean of the test scores in teacher one's class is " + str(np.mean(teacher_one_grades)))
print("The mean of the test scores in teacher two's class is " + str(np.mean(teacher_two_grades)))

print("The variance of the test scores in teacher one's class is " +str(teacher_one_variance))
print("The variance of the test scores in teacher two's class is " +str(teacher_two_variance))

from data import nba_data, okcupid_data

nba_variance = np.var(nba_data)
okcupid_variance = np.var(okcupid_data)

#Change these variables to be the standard deviation of each dataset.
nba_standard_deviation = nba_variance ** 0.5
okcupid_standard_deviation = okcupid_variance ** 0.5

#IGNORE CODE BELOW HERE
print("The standard deviation of the NBA dataset is " +str(nba_standard_deviation))
print("The standard deviation of the OkCupid dataset is " + str(okcupid_standard_deviation))


#DISTRIBUTIONS LESSON::::::
import pandas as pd
# Read in transactions data
transactions = pd.read_csv("transactions.csv")
transactions = transactions.drop(["Unnamed: 0"], axis = 1)

# Save transaction times to a separate numpy array
times = transactions["Transaction Time"].values
cost = transactions["Cost"].values

# Print transactions below
print(transactions)

# Print the average times below
print(np.average(times))

# Find the minimum time, maximum time, and range
min_time = np.min(times)
max_time = np.max(times)
range_time = max_time - min_time

# Printing the values
print("Earliest Time: " + str(min_time))
print("Latest Time: " + str(max_time))
print("Time Range: " + str(range_time))

#Bin size for histograms
# Array of days old bread
days_old_bread = np.array([0, 8, 7, 8, 0, 2, 3, 5, 6, 2])
# Set the minimum and maximums of the array below
min_days_old = 0
max_days_old = 8
# Set the number of bins to 3
bins = 3
# Calculate the bin range
try:
	bin_range = (max_days_old - min_days_old + 1) / bins
	print("Bins: " + str(bins))
	print("Bin Width: " + str(bin_range))
# Printing the values
except:
	print("You have not set the min, max, or bins values yet.")
 
# Count the values in each bin 
days_old_012 = 4
days_old_345 = 2
days_old_678 = 4

# Printing the values
print("Between 0 and 2 days: " + str(days_old_012))
print("Between 3 and 5 days: " + str(days_old_345))
print("Between 6 and 8 days: " + str(days_old_678))

# Use numpy.histogram() below
times_hist = np.histogram(times,range=(0,24),bins=4)

print(times_hist)

# Use plt.hist() below
plt.hist(times,range=(0,24),bins=4)
plt.show()

# Use plt.hist() below
plt.hist(times, range=(0, 24), bins=24,  edgecolor="black")
plt.title("Weekday Frequency of Customers")
plt.xlabel("Hours (1 hour increments)")
plt.ylabel("Count")

plt.show()

from data import dataset

quartile_one = np.quantile(dataset, 0.25) 
quartile_three = np.quantile(dataset, 0.75)
# Define your variables here:
iqr = quartile_three - quartile_one
distance = iqr * 1.5
left_whisker = quartile_one - distance
right_whisker = quartile_three + distance
#Ignore the code below here
try:
  print("The interquartile range of the dataset is " + str(iqr) + ".")
except NameError:
  print("You haven't defined iqr.")
  
try:
  print("Each whisker should be " + str(distance) + " units away from the edges of the box.")
except NameError:
  print("You haven't defined distance.")
  
try:
  print("The left whisker should extend to " + str(left_whisker) + " .")
except NameError:
  print("You haven't defined left_whisker.")
  
try:
  print("The right whisker should extend to " + str(right_whisker) + " .")
except NameError:
  print("You haven't defined right_whisker.")
  
from music_data import two_thousand, two_thousand_one, two_thousand_two

plt.boxplot([two_thousand, two_thousand_one, two_thousand_two], labels = ["2000 Songs", "2001 Songs", "2002 Songs"])
plt.show()

#SUMMARY STATS FOR CATEGORICAL VARIABLES:::
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# Show the first few rows of nyc_trees
print(nyc_trees.head(5))

# Which columns are categorical vars?
categorical_vars = ['status', 'health', 'spc_common', 'neighborhood']

# Get tree counts by neighborhood
tree_counts = nyc_trees.neighborhood.value_counts()
print(tree_counts)
# Get neighborhoods with most trees
greenest_neighborhood = "Annadale-Huguenot-Prince's Bay-Eltingville"

tree_health_statuses = nyc_trees.health.unique()
print(tree_health_statuses)

health_categories = ["Poor","Fair","Good"]

nyc_trees['health'] = pd.Categorical(
        nyc_trees['health'], health_categories, ordered=True
)

median_index = np.median(nyc_trees['health'].cat.codes)
median_health_status = health_categories[int(median_index)]
print(median_health_status)

nyc_trees.tree_diam_category = pd.Categorical(nyc_trees.tree_diam_category, ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)'], ordered=True)

# Get Mean Diam of diameter variable, `trunk_diam`
mean_diam = nyc_trees.trunk_diam.mean()
print(mean_diam)

# Get Mean Category of `tree_diam_category`
mean_diam_cat = nyc_trees.tree_diam_category.cat.codes.mean()
print(mean_diam_cat)

size_labels_ordered = ['Small (0-3in)', 'Medium (3-10in)', 'Medium-Large (10-18in)', 'Large (18-24in)','Very large (>24in)']

nyc_trees.tree_diam_category = pd.Categorical(nyc_trees.tree_diam_category, size_labels_ordered, ordered=True)

# Calculate 25th Percentile Category
p25_ind = np.percentile(nyc_trees.tree_diam_category.cat.codes,25)

p25_tree_diam_category = \
size_labels_ordered[int(p25_ind)]

# Calculate 75th Percentile Category
p75_ind = np.percentile(nyc_trees.tree_diam_category.cat.codes,75)

p75_tree_diam_category = \
size_labels_ordered[int(p75_ind)]

tree_status_proportions = nyc_trees.status.value_counts(normalize=True)
print(tree_status_proportions)

health_proportions = nyc_trees.health.value_counts(dropna=True, normalize=True)
print(health_proportions)

health_proportions_2 = nyc_trees.health.value_counts(dropna=False, normalize=True)
print(health_proportions_2)

living_frequency = np.sum(nyc_trees.status == 'Alive')
living_proportion = (nyc_trees.status == 'Alive').mean()

print(living_frequency)
print(living_proportion)

giant_frequency = np.sum(nyc_trees.trunk_diam > 30)
giant_proportion = (nyc_trees.trunk_diam > 30).mean()

print(giant_frequency)
print(giant_proportion)


# min-max normalisation:
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
 
# read in data 
data = pd.read_csv('data.csv')
 
# normalize data 
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

# standardisation:
from sklearn.preprocessing import StandardScaler
import pandas as pd
 
# read in data 
data = pd.read_csv('data.csv')
 
# standardize data
scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)

# binning variables:
dance_class = pd.read_csv('dance_class_data.csv')
bins = [20, 30, 40, 50, 60, 70]
# Create new binned_age column that bins the values of the ‘Age’ column
dance_class['binned_age'] = pd.cut(dance_class['Age'], bins)
 
# Print the first few rows of the data
print(dance_class[['binned_age', 'Age']].head())

# combining categorical data:
# read in data
election_data = pd.read_csv('election_data.csv')
 
# get the counts for each candidate
votes = election_data['Vote'].value_counts()
print(votes)

mask = election_data.isin(votes[votes < 200].index)
# puts others into a category
election_data[mask] = 'Other'
print(election_data['Vote'].value_counts())

# log transform:
data = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4]
 
# log transform
log_data = np.log(data)
 
print(log_data)
# 0, 0, 0, 0, 0.693, 0.693, 0.693, 1.098, 1.098, 1.386, 1.386

from sklearn.preprocessing import PowerTransformer
 
# log transform 
log_transform = PowerTransformer()
log_transform.fit_transform(data)



