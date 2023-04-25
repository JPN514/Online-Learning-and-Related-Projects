#This is Jeopardy
#cleans the csv file and creates dataframe which can be searched

import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv("jeopardy.csv")

#inspect and alter the column names:
print(jeopardy.head())

new_columns = []
for col in jeopardy.columns:
  new_columns.append(col.strip())
old_columns = []
for col in jeopardy.columns:
  old_columns.append(col)
zip_cols = zip(old_columns,new_columns)
changed_columns = {a : b for (a,b) in zip_cols}
print(changed_columns)
jeopardy.rename(columns=changed_columns,inplace=True)
print(jeopardy.columns)

#Function to search for questions that contain every word in a given list
def filter_for_words(word_list):
  #the lambda checks for each word in the word list against the question string, needs all word from words_list in string to return true
  mylambda = lambda string : all(word.lower() in string.lower() for word in word_list)  
  specific_word_qs = jeopardy[jeopardy.Question.apply(mylambda)]
  print(specific_word_qs)  
  return specific_word_qs
king_of_england = filter_for_words(["King"])


#replaces the string values of "Value" column with floats
jeopardy["Value"] = jeopardy["Value"].apply(lambda x : \
float(x[1:].replace(",","")) if x != "None" else 0)


#counts the unique answers and sorts the dataframe into descending order 
def find_unique_answers(question):
  unique_ans = question.groupby("Answer").Category.count().reset_index()
  unique_ans.sort_values("Category",inplace=True,ascending=False)
  unique_ans.rename(columns={"Category":"Count"},inplace=True)
  print(unique_ans)
  return unique_ans

ans_count = find_unique_answers(king_of_england)  




