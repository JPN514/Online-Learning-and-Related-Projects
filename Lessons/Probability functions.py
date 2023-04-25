#Probability functions:

def prob_a_or_b(a, b, all_possible_outcomes):
  # probability of event a
  prob_a = len(a)/len(all_possible_outcomes)
	
	# probability of event b
  prob_b = len(b)/len(all_possible_outcomes)
	
	# intersection of events a and b
  inter = a.intersection(b)
	
	# probability of intersection of events a and b
  prob_inter = len(inter)/len(all_possible_outcomes)
	
	# add return statement here
  return prob_a + prob_b - prob_inter

# rolling a die once and getting an even number or an odd number
evens = {2, 4, 6}
odds = {1, 3, 5}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# call function here first
print(prob_a_or_b(evens,odds,all_possible_rolls))

# rolling a die once and getting an odd number or a number greater than 2
odds = {1, 3, 5}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# call function here second
print(prob_a_or_b(odds,greater_than_two,all_possible_rolls))

# selecting a diamond card or a face card from a standard deck of cards
diamond_cards = {'ace_diamond', '2_diamond', '3_diamond', '4_diamond', '5_diamond', '6_diamond', '7_diamond', '8_diamond', '9_diamond', '10_diamond', 'jack_diamond', 'queen_diamond', 'king_diamond'}
face_cards = {'jack_diamond', 'jack_spade', 'jack_heart', 'jack_club', 'queen_diamond', 'queen_spade', 'queen_heart', 'queen_club', 'king_diamond', 'king_spade', 'king_heart', 'king_club'}
# all cards in a deck representing the entire sample space
all_possible_cards = {'ace_diamond', '2_diamond', '3_diamond', '4_diamond', '5_diamond', '6_diamond', '7_diamond', '8_diamond', '9_diamond', '10_diamond', 'jack_diamond', 'queen_diamond', 'king_diamond', 'ace_heart', '2_heart', '3_heart', '4_heart', '5_heart', '6_heart', '7_heart', '8_heart', '9_heart', '10_heart', 'jack_heart', 'queen_heart', 'king_heart', 'ace_spade', '2_spade', '3_spade', '4_spade', '5_spade', '6_spade', '7_spade', '8_spade', '9_spade', '10_spade', 'jack_spade', 'queen_spade', 'king_spade', 'ace_club', '2_club', '3_club', '4_club', '5_club', '6_club', '7_club', '8_club', '9_club', '10_club', 'jack_club', 'queen_club', 'king_club'}

# call function here third
print(prob_a_or_b(diamond_cards,face_cards,all_possible_cards))


#DIE rolls:
import numpy as np

# create 6 sided "die"
die_6 = range(1, 7)

# set number of rolls
num_rolls = 10

# roll the "die" the set amount of times
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
print(results_1)

# create 12-sided "die"
die_12 = range(1,13)

# roll the 12-sided "die" 10 times
results_2 = np.random.choice(die_12, size = num_rolls, replace = True)

import scipy.stats as stats

## Checkpoint 1, prob of observing 4 to 6 heads from 10 flips: 
prob_1 = stats.binom.pmf(4,10,0.5) + stats.binom.pmf(5,10,0.5) + stats.binom.pmf(6,10,0.5)
print(prob_1)

## Checkpoint 2, prob of observing more than 2 heads
prob_2 = 1 - stats.binom.pmf(0,10,0.5) - \
stats.binom.pmf(1,10,0.5) - stats.binom.pmf(2,10,0.5)  
print(prob_2)

## Checkpoint 1, prob of 3 or fewer heads from 10 coin flips:
prob_1 = stats.binom.cdf(3,10,0.5)
print(prob_1)

# compare to pmf code
print(stats.binom.pmf(0, n=10, p=.5) + stats.binom.pmf(1, n=10, p=.5) + stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5))

## Checkpoint 2, prob of more than 5 heads from 10 flips:
prob_2 = 1 - stats.binom.cdf(5,10,0.5)
print(prob_2)

## Checkpoint 3, observe between 2 and 5 heads from 10 flips:
prob_3 = stats.binom.cdf(5,10,0.5) - stats.binom.cdf(1,10,0.5) 
print(prob_3)

# compare to pmf code
#print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5) + stats.binom.pmf(5, n=10, p=.5))

#normal distribution P(X<=175), where N(167.64,8):
prob = stats.norm.cdf(175,167.64,8)
print(prob)

## Checkpoint 1, temperature between 18 and 25 degrees:
temp_prob_1 = stats.norm.cdf(25,20,3) - stats.norm.cdf(18,20,3)
print(temp_prob_1)


## Checkpoint 2, temperature is greater than 24 degrees:
temp_prob_2 = 1 - stats.norm.cdf(24,20,3)
print(temp_prob_2)

#Poisson distribution:

## Checkpoint 1
# calculate prob_15
prob_15 = stats.poisson.pmf(15,15) 

print(prob_15)


## Checkpoint 
# calculate prob_7_to_9
prob_7_to_9 = stats.poisson.pmf(7,15) + stats.poisson.pmf(8,15) + stats.poisson.pmf(9,15)

print(prob_7_to_9)

## Checkpoint 1
# calculate prob_more_than_20
prob_more_than_20 = 1 - stats.poisson.cdf(20,15) 

print(prob_more_than_20)

## Checkpoint 
# calculate prob_17_to_21
prob_17_to_21 = stats.poisson.cdf(21,15) - stats.poisson.cdf(16,15)

print(prob_17_to_21)

from histogram_function import histogram_function

## Checkpoint 1
# lambda = 15, 1000 random draws 
rand_vars = stats.poisson.rvs(15,size=1000) #runs a sample of 1000 random Poisson variables with lambda=15 

## Checkpoint 2
# print the mean of rand_vars
print(rand_vars.mean())

## Checkpoint 3
histogram_function(rand_vars)

## For checkpoints 1 and 2
# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)

## Checkpoint 1
# print variance of rand_vars_7
print(np.var(rand_vars_7))

## Checkpoint 2
# print minimum and maximum of rand_vars_7
print(min(rand_vars_7),max(rand_vars_7))

## For checkpoints 3 and 4
# 5000 draws, lambda = 17
rand_vars_17 = stats.poisson.rvs(17, size = 5000)

## Checkpoint 3
# print variance of rand_vars_17
print(np.var(rand_vars_17))

## Checkpoint 4
# print minimum and maximum of rand_vars_17
print(min(rand_vars_17),max(rand_vars_17))

## Checkpoint 1
expected_bonus = 75000 * 0.08
print(expected_bonus)

## Checkpoint 2
num_goals = stats.poisson.rvs(4,size=100)

## Checkpoint 3
print(np.var(num_goals))

## Checkpoint 4
num_goals_2 = 2 * num_goals
print(np.var(num_goals_2))

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

population = pd.read_csv("salmon_population.csv")
population = np.array(population.Salmon_Weight)
pop_mean = round(np.mean(population),3)

## Plotting the Population Distribution
sns.histplot(population, stat='density')
plt.axvline(pop_mean,color='r',linestyle='dashed')
plt.title(f"Population Mean: {pop_mean}")
plt.xlabel("Weight (lbs)")
plt.show()
plt.clf() # close this plot

samp_size = 30
# Generate our random sample below
sample = np.random.choice(np.array(population), samp_size, replace = False)

### Define sample mean below
sample_mean = round(sample.mean(),3)

### Uncomment the lines below to plot the sample data:
sns.histplot(sample, stat='density')
plt.axvline(sample_mean,color='r',linestyle='dashed')
plt.title(F"Sample Mean: {sample_mean}")
plt.xlabel("Weight (lbs)")
plt.show()

population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = population['Cod_Weight']

sample_size = 50
sample_means = []

for i in range(500):
  samp = np.random.choice(population, sample_size, replace = False)
  this_sample_mean = samp.mean()
  sample_means.append(this_sample_mean)

sns.histplot(sample_means,stat='density')
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()

cod_population = pd.read_csv("cod_population.csv")
# Save transaction times to a separate numpy array
population = cod_population['Cod_Weight']

## Checkpoint 1:
sns.histplot(population, stat = 'density' )
plt.title("Population Distribution")
plt.show()

sample_means = []

# Below is our sample size
samp_size = 50

for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    this_sample_mean = np.mean(samp)
    sample_means.append(this_sample_mean)

## Checkpoint 2
plt.clf() # this closes the previous plot
sns.histplot(sample_means, stat = 'density' )
plt.title("Sampling Distribution of the Mean")
plt.xlabel("Weight (lbs)")
plt.show()

population_mean = 36
population_std_dev = 10
# Set the sample size:
samp_size = 50

### Below is code to create simulated dataset and calculate Standard Error

# Create the population
population = np.random.normal(population_mean, population_std_dev, size = 100000)

## Simulate the sampling distribution
sample_means = []
for i in range(500):
    samp = np.random.choice(population, samp_size, replace = False)
    sample_means.append(np.mean(samp))

mean_sampling_distribution = round(np.mean(sample_means),3)
std_sampling_distribution = round(np.std(sample_means),3)

std_error = population_std_dev / (samp_size **0.5)

sns.histplot(population, stat = 'density')
plt.title(f"Population Mean: {population_mean} \n Population Std Dev: {population_std_dev} \n Standard Error = {population_std_dev} / sq rt({samp_size}) \n Standard Error = {std_error} ")
plt.xlim(-50,125)
plt.ylim(0,0.045)
plt.show()
plt.clf()

## Plot the sampling distribution
sns.histplot(sample_means, stat = 'density')
# calculate the mean and SE for the probability distribution
mu = np.mean(population)
sigma = np.std(population)/(samp_size**.5)

# plot the normal distribution with mu=popmean, sd=sd(pop)/sqrt(samp_size) on top
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), color='k', label = 'normal PDF')
# plt.axvline(mean_sampling_distribution,color='r',linestyle='dashed')
plt.title(f"Sampling Dist Mean: {mean_sampling_distribution} \n Sampling Dist Standard Deviation: {std_sampling_distribution}")
plt.xlim(20,50)
plt.ylim(0,0.3)
plt.show()

## Setting up our parameters
std_dev = 20 
samp_size = 25
standard_error = 20 / (25**.5)
cod_cdf = stats.norm.cdf(30,36,standard_error)
print(cod_cdf)

#hypothesis testing:

prices = np.genfromtxt("prices.csv")
# print prices:
print(prices)
# calculate prices_mean and print it out:
prices_mean = prices.mean()
print(prices_mean)


from scipy.stats import ttest_1samp
prices_mean = np.mean(prices)
print("mean of prices: " + str(prices_mean))
# use ttest_1samp to calculate pval
tstat, pval = ttest_1samp(prices,1000) 
# print pval
print(pval) #0.49 which makes sense 

#plot your histogram here
plt.hist(prices)
plt.show()

#BINOMIAL TEST:

monthly_report = pd.read_csv('monthly_report.csv')
#print the head of monthly_report:
print(monthly_report.head())

#calculate and print sample_size:
sample_size = len(monthly_report)
print(sample_size)

#calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == "y")
print(num_purchased)

#simulate one visitor:
one_visitor = np.random.choice(["y","n"],size=1,\
p=[0.1,0.9])
print(one_visitor)

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(["y","n"],size=500,\
p=[0.1,0.9])
print(simulated_monthly_visitors)

#calculate the number of simulated visitors who made a purchase:
num_purchased = sum(simulated_monthly_visitors == "y")
print(num_purchased)

#run null hypothesis 10000 times
null_outcomes = []
#start for loop here:
for i in range(0,10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)

#calculate the minimum and maximum values in null_outcomes here:
null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)
print(null_min, null_max)

#plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(41, color = 'r') #red vertical line at 41
plt.show()

#calculate the 90% interval here:
null_90CI = np.percentile(null_outcomes, [5,95]) #cuts off the tails of the sample distribution, removing the outliers 
print(null_90CI)

#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41)/len(null_outcomes)  #41 is the observed number of purchases from above
print(p_value)

#calculate the p-value here:
#this p-value is two sided about the observed 41 purchases from earlier
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | \
(null_outcomes >= 59))/len(null_outcomes) 
print(p_value)

#binom test function:
from scipy.stats import binom_test
def simulation_binomial_test(observed_successes,n,p):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  #calculate a 1-sided p-value
  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  
  #return the p-value
  return p_value

#Test your function below by uncommenting the code below. You should see that your simulation function gives you a very similar answer to the binom_test function from scipy:

p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)

# calculate p_value_2sided here:
p_value_2sided = binom_test(41, 500, .1)
print(p_value_2sided)

p_value_1sided = binom_test(41, 500, .1, alternative = 'less')
print(p_value_1sided)

# P-Value for first Hypothesis Test
p_value1 = .062
# Set the correct value for p_value1_significance
p_value1_significance = 'not significant'

# P-Value for second Hypothesis Test
p_value2 = 0.013
# Set the correct value for p_value2_significance
p_value2_significance = 'significant'

# P-Value for first Hypothesis Test
p_value1 = .062
# Set the correct value for remove_question_1
remove_question_1 = "no"

# P-Value for second Hypothesis Test
p_value2 = 0.013
# Set the correct value for remove_question_2
remove_question_2 = "yes"

# Import libraries
import numpy as np
from scipy.stats import binom_test

# Initialize num_errors
false_positives = 0
# Set significance threshold value
sig_threshold = 0.01

# Run binomial tests & record errors
for i in range(1000):
    sim_sample = np.random.choice(['correct', 'incorrect'], size=100, p=[0.8, 0.2])
    num_correct = np.sum(sim_sample == 'correct')
    p_val = binom_test(num_correct, 100, .8)
    if p_val < sig_threshold:
        false_positives += 1

# Print proportion of type I errors 
print(false_positives/1000)

# Set a correct value for num_tests_50percent
num_tests_50percent = 15

#plot showing num of tests and prob of a type 1 error on null hypothesis
# Create the plot
sig_threshold = 0.10
num_tests = np.array(range(50))
probabilities = 1-((1-sig_threshold)**num_tests)
plt.plot(num_tests, probabilities)

# Edit title and axis labels
plt.title('Type I Error Rate for Multiple Tests', fontsize=15)
# Label the y-axis
plt.ylabel('Probability of at Least One Type I Error', fontsize=12)
# Label the x-axis
plt.xlabel('Number of Tests', fontsize=12)

# Show the plot                
plt.show()



#LINEAR REGRESSION:

# Read in the data
students = pd.read_csv('test_data.csv')

# Write equation for a line
y = 9.85 * students.hours_studied + 43 #we plot this on the scatter below

# Create the plot here: 
plt.scatter(students.hours_studied,students.score)
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.plot(students.hours_studied, y)
plt.show()

# Write equation for a line
predicted_score = 10 * students.hours_studied + 45

# Create the plot
plt.scatter(students.hours_studied, students.score)
plt.plot(students.hours_studied, predicted_score)
plt.show()


#LINEAR REGRESSION MODEL TO FIND LINE OF BEST FIT:
import statsmodels.api as sm
# Create the model here:
model = sm.OLS.from_formula("score~hours_studied",data=students) #scores as the outcome using hours studied as the predictor
# Fit the model here:
results = model.fit()
# Print the coefficients here:
print(results.params) #tells us the y intercept and the gradient of the line of best fit 
#predict values using the model created above
# Calculate and print `pred_3hr` here:
pred_3hr = results.params[1] * 3 + results.params[0]
print(pred_3hr)
# Calculate and print `pred_5hr` here:
newdata = {"hours_studied":[5]}
pred_5hr = results.predict(newdata)
print(pred_5hr)

# Calculate `fitted_values` here:
fitted_values = results.predict(students) #these are the values predicted for each person in the dataset that was used to fit the model
print(fitted_values.head())
# Calculate `residuals` here:
residuals = students.score - fitted_values #residuals are the differences between the true values and the predicted values 
print(residuals.head()) #positive residual means true value was above line, negative residual means true value was below the line

# Plot a histogram of the residuals here:
plt.hist(residuals) #looks approx normal, so the normality assumption(residuals should be normally dist.) is met.
plt.show()
plt.clf()

# Plot the residuals against the fitted vals here:
plt.scatter(fitted_values,residuals) #checks for hommoscedasticity assumption- that residuals have equal variation across all the values of the predictor variable. NO pattern here, so the assumption is met. 
plt.show()

#categorical groups below ie breakfast or no breakfast:
# Calculate group means
print(students.groupby('breakfast').mean().score)
# Create the scatter plot here:
plt.scatter(students.breakfast,students.score)
plt.xlabel("Breakfast")
# Add the additional line here:
plt.plot([0,1], [61.664151, 73.721277]) #line of best fit intersects the mean of each group!!!
# Show the plot
plt.show()

# Calculate and print group means
mean_score_no_breakfast = np.mean(students.score[students.breakfast == 0])
mean_score_breakfast = np.mean(students.score[students.breakfast == 1])
print('Mean score (no breakfast): ', mean_score_no_breakfast)
print('Mean score (breakfast): ', mean_score_breakfast)

# Fit the model and print the coefficients
model = sm.OLS.from_formula('score ~ breakfast', data=students)
result = model.fit()
print(result.params)
# Calculate and print the difference in group means
print(mean_score_breakfast - mean_score_no_breakfast)

