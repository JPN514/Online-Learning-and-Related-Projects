#Heart disease research part 1

#analysis of heart disease data from a csv file using statistical methods

# import libraries
import codecademylib3
import pandas as pd
import numpy as np

# load data
heart = pd.read_csv('heart_disease.csv')
yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']
print(heart.head())

#cholesterol for patients WITH heart disease:
chol_hd = yes_hd.chol

#mean chol level:
mean_chol = chol_hd.mean()
print(mean_chol)

#hypothesis test for >=240 chol level on average:
#NULL hyp: average chol is equal to 240
#ALT hyp: average chol is greater than 240
from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_hd,240)
print(pval/2) #significant so reject NULL hypothesis 

#cholesterol for patients WITHOUT heart disease:
chol_no = no_hd.chol
#mean:
mean_chol_no = chol_no.mean()
print(mean_chol_no)

#hypothesis test for >=240 chol level on average:
#NULL hyp: average chol is equal to 240
#ALT hyp: average chol is greater than 240
from scipy.stats import ttest_1samp
tstat, pval = ttest_1samp(chol_no,240)
print(pval/2) #not significant so believe NULL hypothesis

#full dataset again:
num_patients = len(heart)
print(num_patients)

#number of patients with fasting blood sugar >120:
num_highfbs_patients = len(heart[heart.fbs == 1.0])
print(num_highfbs_patients)

# calculate 8% of sample size
print(0.08*num_patients)

#binomial test on the 8% sample:
from scipy.stats import binom_test
pval = binom_test(num_highfbs_patients, num_patients, .08, alternative='greater')
print(pval)

