#DATA WRANGLING LESSON:::

#Regular expressions:::
#see cheatsheet in files 

#HOW TO CLEAN DATA WITH PYTHON:::
import codecademylib3_seaborn
import pandas as pd

df1 = pd.read_csv("df1.csv")
df2 = pd.read_csv("df2.csv")

print(df1.head())
print(df2.head())
clean = 2

import glob #glob allows us to cluster together several files in order to loop through them and create a dataframe from them 

student_files = glob.glob("exams*.csv")
df_list = [] 
for filename in student_files:
  data = pd.read_csv(filename)
  df_list.append(data)
students = pd.concat(df_list)
print(students, len(students))  

from students import students
#pd.melt allows us to transform df so each variable is a separate column and each row is a separate observation
#frame= frame to transform, id_vars= columns to preserve, value_vars= the columns being turn into variables, value_name= name of column storing new values, 
#var_name= name of column storing new values.
#in this case, the df had each student with a fractions and prob observation in the same row,
#this then makes a column "exams" with values of "fractions" or "probabilities" with a row for each of these options for each student
#makes "score" column with the corresponding scores from each frac/prob as the values in the column  
print(students.columns)
students = pd.melt(frame=students, id_vars=["full_name","gender_age","grade"],value_vars=["fractions","probability"],value_name="score",var_name="exam")
print(students.head())
print(students.columns)
print(students.exam.value_counts())

print(students)
duplicates = students.duplicated() #returns a series telling us true/false (duplicate or not) for each row 
print(duplicates)
print(duplicates.value_counts())
students = students.drop_duplicates() #removes the duplicates from the dataframe
print(duplicates.value_counts())

print(students.columns)
print(students.gender_age.head())               #below splits the gender_age column into two separate columns
students['gender'] = students.gender_age.str[0] 
students['age'] = students.gender_age.str[1:]
print(students.head())
students = students[['full_name','exam','grade','score','gender','age']]

name_split = students.full_name.str.split(" ") #this splits the full_name column so we can produce a first and last name for each student
students["first_name"] = name_split.str.get(0)
students["last_name"] = name_split.str.get(1) 
print(students.head())

students.score = students["score"].replace("%","",regex=True) #regex to replace the % signs with nothing (essentially remove them)
students.score = pd.to_numeric(students.score)                #convert the score column to numeric data to enable us to calculate mean etc

students.grade = students.grade.str.split("(\d+)",expand=True)[1] #more regex to get the numerical part of a string of form "11th grade"
print(students.dtypes)
students.grade = pd.to_numeric(students.grade)
avg_grade = students.grade.mean()
print(avg_grade)

score_mean = students.score.mean()
students.score = students.score.fillna(0) #fills all the nan values with 0
score_mean_2 = students.score.mean()
print(score_mean, score_mean_2)


