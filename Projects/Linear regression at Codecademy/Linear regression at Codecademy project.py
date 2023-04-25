#Linear regression at Codecademy project

# Load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import codecademylib3

# Read in the data
codecademy = pd.read_csv('codecademy.csv')

# Print the first five rows
print(codecademy.head())
# Create a scatter plot of score vs completed
plt.scatter(codecademy.completed,codecademy.score)
plt.xlabel("Completed")
plt.ylabel("Score")
# Show then clear plot
plt.show()
plt.clf()
# Fit a linear regression to predict score based on prior lessons completed
model = sm.OLS.from_formula("score ~ completed",data=codecademy)
result = model.fit()
print(result.params)
# Intercept interpretation:
View1 = "If the student has completed 0 other items on Codecademy prior to the quiz, we can expect them to score ~13 points."
# Slope interpretation:
View2 = "For 1 extra item of content completed, the student will be expected to score ~1.31 more points on the quiz."
# Plot the scatter plot with the line on top
y = result.params[1] * codecademy.completed + result.params[0] #equation of the regression line 
plt.scatter(codecademy.completed,codecademy.score)
plt.xlabel("Completed")
plt.ylabel("Score")
plt.plot(codecademy.completed,y)
# Show then clear plot
plt.show()
plt.clf()

# Predict score for learner who has completed 20 prior lessons
t20_lessons_score = result.params[1] * 20 + \
result.params[0]
print(t20_lessons_score)
# Calculate fitted values
fitted_values = result.predict(codecademy)
# Calculate residuals
residuals = codecademy.score - fitted_values
# Check normality assumption
plt.hist(residuals)
plt.title("Residuals of Codecademy scores")
plt.show()
plt.clf()

# Check homoscedasticity assumption
plt.scatter(fitted_values,residuals)
plt.show()
plt.clf() #met as no apparent patterns in the scatter plot

# Create a boxplot of score vs lesson
sns.boxplot(x="lesson",y="score",data=codecademy)
plt.title("Score by lesson")
# Show then clear plot
plt.show()
plt.clf()

# Fit a linear regression to predict score based on which lesson they took
model = sm.OLS.from_formula("score ~ lesson",data=codecademy)
result = model.fit()
print(result.params)

# Calculate and print the group means and mean difference (for comparison)
mean_score_A = np.mean(codecademy.score[codecademy.lesson == "Lesson A"])
mean_score_B = np.mean(codecademy.score[codecademy.lesson == "Lesson B"])
print(mean_score_A,mean_score_B,mean_score_A-mean_score_B)

# Use `sns.lmplot()` to plot `score` vs. `completed` colored by `lesson`
sns.lmplot(x = 'completed', y = 'score', hue = 'lesson', data = codecademy)
plt.show()