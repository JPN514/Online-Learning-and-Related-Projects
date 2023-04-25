#Data science foundations part 2

#LAMBDA FUNCTIONS

#Write your lambda function here
contains_a = lambda word : "a" in word
print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))

#Write your lambda function here
long_string = lambda str : len(str) > 12
print(long_string("short"))
print(long_string("photosynthesis"))

#Write your lambda function here
ends_in_a = lambda str : str[-1] == "a"
print(ends_in_a("data"))
print(ends_in_a("aardvark"))

#Write your lambda function here
double_or_zero = lambda num : 2*num if num > 10 else 0
print(double_or_zero(15))
print(double_or_zero(5))

#Write your lambda function here
even_or_odd = lambda num : "even" if num % 2 == 0 else "odd"
print(even_or_odd(10))
print(even_or_odd(5))

#Write your lambda function here
multiple_of_three = lambda num : "multiple of three" if num % 3 == 0 else "not a multiple"
print(multiple_of_three(9))
print(multiple_of_three(10))

#Write your lambda function here
rate_movie = lambda rating : "I liked this movie" if rating > 8.5 else "This movie was not very good"
print(rate_movie(9.2))
print(rate_movie(7.2))

#Write your lambda function here
ones_place = lambda num : num % 10 
print(ones_place(123))
print(ones_place(4))

#Write your lambda function here
double_square = lambda num : 2 * (num**2) 
print(double_square(5))
print(double_square(3))

import random
#Write your lambda function here
add_random = lambda num : num + random.randint(1,10)
print(add_random(5))
print(add_random(100))

#DATAFRAMES BASICS

#import codecademylib3
import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ["t-shirt","t-shirt","skirt","skirt"],
  "Color": ["blue","green","red","black"]
})
print(df1)
#pass in data as a list of lists 
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3,"San Francisco",90],
  [4,"Sacramento",115]
],
  columns=["Store ID",
    "Location",
    "Number of Employees"
  ])
print(df2)

#read a csv file into a dataframe 
#df = pd.read_csv("sample.csv")
#print(df)

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north = df["clinic_north"]
print(type(clinic_north)) #type: series (column)
print(type(df)) #type: frame (dataframe)

clinic_north_south = df[["clinic_north","clinic_south"]]
print(type(clinic_north_south)) #type: frame as two columns

march = df.iloc[2] #selects the row of "March", which is the 3rd row (index 2)
print(march)

april_may_june = df[3:] #selects from the 3rd row onwards (inclusive)
print(april_may_june)

january = df[df["month"] == "January"] #logic condition to select the month of January 
print(january)

march_april = df[(df["month"] == "March")|
(df["month"] == "April")] #logic OR comndition remember brackets and df inside []
print(march_april)

january_february_march = df[df["month"].isin(["January","February","March"])] #isin checks for column "month" in the list contents
print(january_february_march)

#Altering the columns of the subframe
df2 = df.loc[[1, 3, 5]]
df3 = df2.reset_index()
print(df3)
df2.reset_index(inplace = True, drop = True) #drops index column and resets the left most indicies
print(df2)

#Adding a column to the df called "sold in bulk?"
df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
df["Sold in Bulk?"] = ["Yes","Yes","No","No"]
df["Is taxed?"] = "Yes" #adds a new column with the same entry for each row "Yes"
df["Margin"] = df["Price"] - df["Cost to Manufacture"] #adds new column using an operation on the other columns
print(df)

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])
df["Lowercase Name"] = df["Name"].apply(str.lower) #adds new column by applying a string operation to an exsiting column 
print(df)

#below applies a lambda function to an existing column to produce a new column 
#df = pd.read_csv('employees.csv')
#get_last_name = lambda string : string.split(" ")[-1]
#df["last_name"] = df["name"].apply(get_last_name)
#print(df)

#Another more complex lambda function 
total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
#df['total_earned'] = df.apply(total_earned, axis = 1) #axis = 1 takes an entrie row as an entry as opposed to a column

#df.columns = ["ID", "Title", "Category", "Year Released", "Rating"] #rename all the columns of a dataframe at once 

#df.rename(columns={"name":"movie_title"},inplace=True)
#inplace modifies the df instead of creating a new dataframe

#mylambda = lambda row : "vegan" if row != "leather" else "animal" 
#orders["shoe_source"] = orders["shoe_material"].apply(lambda row : "vegan" if row != "leather" else "animal")
#mylambda1 = lambda row : ("Dear Mr. {}".format(row["last_name"])) if row.gender == "male" else ("Dear Ms. {}".format(row["last_name"]))
#orders["salutation"] = orders.apply(mylambda1,axis = 1)

orders = pd.read_csv('orders.csv')
print(orders.head(10))

most_expensive = orders.price.max() #maximum value 
num_colors = orders.shoe_color.nunique() #number of unnique values

pricey_shoes = orders.groupby("shoe_type").price.max() #groups the shoes by their types and returns the priciest
print(pricey_shoes) #e.g. the most expensive trainers and most expensive sandals

pricey_shoes = orders.groupby('shoe_type').price.max().reset_index() #sets the grouped_by category and price as the column names
print(pricey_shoes)
import numpy as np
cheap_shoes = orders.groupby("shoe_color").price.apply(lambda x: np.percentile(x,25)).reset_index() #can apply a lambda function, reset_index ensures that cheap_shoes is a dataframe rather than a series 
print(cheap_shoes)

shoe_counts = orders.groupby(["shoe_type","shoe_color"]).id.count().reset_index() #counts the number of each shoe sold grouped by type and colour e.g. 12 red wedges and 34 blue wedges
print(shoe_counts)

#below creates a pivot table from the above, makes the info more readable 
shoe_counts_pivot = shoe_counts.pivot(columns = "shoe_color", index = "shoe_type", values = "id").reset_index()
print(shoe_counts_pivot)

user_visits = pd.read_csv('page_visits.csv')
print(user_visits.head())


click_source = user_visits.groupby("utm_source").id.count().reset_index()
print(click_source)
click_source_by_month = user_visits.groupby(["utm_source","month"]).id.count().reset_index()
print(click_source_by_month)
click_source_by_month_pivot = click_source_by_month.pivot(columns = "month", index = "utm_source", values = "id").reset_index() #another pivot table 
print(click_source_by_month_pivot)

#MULTIPLE DATAFRAMES/TABLES SIMILAR TO SQL 

sales = pd.read_csv('sales.csv')
print(sales)
targets = pd.read_csv('targets.csv')
print(targets)

sales_vs_targets = pd.merge(sales,targets) #finds common columns from the two dataframes then merges their rows
print(sales_vs_targets)
crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target] #all rows where sales > targets 

men_women = pd.read_csv('men_women_sales.csv')
all_data = sales.merge(targets).merge(men_women) #merges all the tables together from left to right
print(all_data)
results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)
orders_products = pd.merge(orders,products.rename(columns={"id" : "product_id"})) #renames the columns as we merge the tables 
print(orders_products)

orders_products = pd.merge(orders,products,left_on="product_id", \
right_on="id",suffixes=["_orders","_products"]) #allows us to change the columns names by adding a suffix and joining on a specific column
print(orders_products)

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)
store_a_b_outer = pd.merge(store_a,store_b,how="outer") #outer join keeps the unmatched rows from both tables  
print(store_a_b_outer)

store_a_b_left = pd.merge(store_a,store_b,how="left") 
#keeps all left table (in this case store_a) and only the matched rows from the right table, anything right table does not have is NULL or NAN
print(store_a_b_left)

store_b_a_left = pd.merge(store_b,store_a,how="left")
print(store_b_a_left)

bakery = pd.read_csv('bakery.csv')
print(bakery)
ice_cream = pd.read_csv('ice_cream.csv')
print(ice_cream)
menu = pd.concat([bakery,ice_cream]) #concatenates the dataframes. NOTE the columns must be matching
print(menu)

visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])
print(visits)
print(checkouts)
v_to_c = pd.merge(visits,checkouts)
v_to_c["time"] = v_to_c["checkout_time"] - v_to_c["visit_time"]
print(v_to_c["time"].mean()) 

#change data types
# Import dataset as a Pandas dataframe
movies = pd.read_csv("netflix_movies.csv")

# View the first five rows of the dataframe
print(movies.head())

# Print the data types
print(movies.dtypes)

# Fill in the missing cast_count values with 0
movies['cast_count'].fillna(0, inplace = True)

# Change the type of the cast_count column
movies["cast_count"].astype("int64")

# Check the data types of the columns again. 
print(movies.dtypes)

# Print the unique values of the rating column
print(movies['rating'].unique())

# Change the data type of `rating` to category
movies['rating'] = pd.Categorical(movies['rating'], ['NR', 'G','PG','PG-13','R'], ordered=True)

# Recheck the values of `rating` with .unique()
print(movies.rating.unique())

# Import dataset as a Pandas Dataframe
cereal = pd.read_csv('cereal.csv', index_col=0)

# Show the first five rows of the `cereal` dataframe
print(cereal.head())

# Create a new dataframe with the `mfr` variable One-Hot Encoded, takes mfr column and creates new binary column to reflect the entries in original mfr column 
cereal = pd.get_dummies(data=cereal,columns=["mfr"])

# Show first five rows of new dataframe
print(cereal.head())

auto = pd.read_csv('autos.csv', index_col=0)
# Print the first 10 rows of the auto dataset
print(auto.head(10))

# Print the data types of the auto dataframe
print(auto.dtypes)

# Change the data type of price to float
auto.price.astype("float")

# Set the engine_size data type to category
auto["engine_size"] = pd.Categorical(auto["engine_size"],["small","medium","large"],ordered=True)

# Create the engine_codes variable by encoding engine_size
auto['engine_codes'] = auto['engine_size'].cat.codes
print(auto.head())
# One-Hot Encode the body-style variable
auto = pd.get_dummies(auto, columns = ['body-style'])
# Check the order of the type column
print(auto.head())

#TRIM MEAN
from scipy.stats import trim_mean
movies = pd.read_csv('movies.csv')

# Save the mean to mean_budget
mean_budget = movies["production_budget"].mean()
print(mean_budget)
# Save the median to med_budget
med_budget = movies["production_budget"].median()
print(med_budget)
# Save the mode to mode_budget
mode_budget = movies["production_budget"].mode()
print(mode_budget)
# Save the trimmed mean to trmean_budget
trmean_budget = trim_mean(movies.production_budget, proportiontocut=0.2) #trims off the extreme points, this case 20%
print(trmean_budget)

# Save the range to range_budget
range_budget = movies.production_budget.max() - movies.production_budget.min() 
print(range_budget)
# Save the interquartile range to iqr_budget
iqr_budget = movies.production_budget.quantile(0.75) - movies.production_budget.quantile(0.25)
print(iqr_budget)

# Save the variance to var_budget
var_budget = movies.production_budget.var()
print(var_budget)

# Save the standard deviation to std_budget
std_budget = movies.production_budget.std()
print(std_budget)

# Save the mean absolute deviation to mad_budget
mad_budget = movies.production_budget.mad()
print(mad_budget)

import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv('movies.csv')

# Create a boxplot for movie budget 
sns.boxplot(x="production_budget", data=movies)
plt.show()
plt.close()
# Create a histogram for movie budget
sns.histplot(x="production_budget",data=movies)
plt.show()
plt.close()

genre_counts = movies["genre"].value_counts() #prints how many films of each genre
print(genre_counts)

#Save the proportions to genre_props
genre_props = movies.genre.value_counts() / len(movies.genre)
print(genre_props)

#Create a bar chart for movie genre 
sns.countplot(x="genre",data=movies)
plt.show()
plt.close()

# Create a pie chart for movie genre
movies.genre.value_counts().plot.pie()
plt.show()
plt.close()


students = pd.read_csv('students.csv')
#separate out scores for students who live in urban and rural locations:
scores_urban = students.G3[students["address"]=="U"]
scores_rural = students.G3[students["address"]=="R"]

#calculate means for each group:
scores_urban_mean = scores_urban.mean()
scores_rural_mean = scores_rural.mean()

#print mean scores:
print('Mean score - students w/ urban address:')
print(scores_urban_mean)
print('Mean score - students w/ rural address:')
print(scores_rural_mean)

#calculate mean difference:
mean_diff = scores_urban_mean - scores_rural_mean

#print mean difference
print('Mean difference:')
print(mean_diff)

#calculate medians for each group:
scores_urban_median = scores_urban.median()
scores_rural_median = scores_rural.median()

#print median scores
print('Median score - students w/ urban address:')
print(scores_urban_median)
print('Median score - students w/ rural address:')
print(scores_rural_median)

#calculate median difference
median_diff = scores_urban_median - scores_rural_median

#print median difference
print('Median difference:')
print(median_diff)

#create the boxplot here:
sns.boxplot(data=students,x="address",y="G3") #side by side boxplot 
plt.show()
plt.close()

#create the overlapping histograms here:
plt.hist(scores_urban, color="blue", label="Urban",normed=True,alpha=0.5)
plt.hist(scores_rural, color="red", label="Rural",normed=True,alpha=0.5)
plt.legend()
plt.show()
plt.close()

#create the box-plot here:
sns.boxplot(data=students, x="Fjob", y="G3")
plt.show()
plt.close()


housing = pd.read_csv('housing_sample.csv')
#print the first 10 rows of data:
print(housing.head(10))

#create your scatter plot here:
plt.scatter(x=housing.beds,y=housing.sqfeet)
plt.xlabel("No. of beds")
plt.ylabel("Square ft.")
plt.show()
plt.close()

# calculate and print covariance matrix:
cov_mat_sqfeet_beds = np.cov(housing.sqfeet,housing.beds)
print(cov_mat_sqfeet_beds)
# store the covariance as cov_sqfeet_beds
cov_sqfeet_beds = 228.2

from scipy.stats import pearsonr
#calculate corr_sqfeet_beds and print it out:
corr_sqfeet_beds, p = pearsonr(housing.sqfeet,housing.beds)
print(corr_sqfeet_beds)

# create the scatter plot here:
plt.scatter(x=housing.beds,y=housing.sqfeet)
plt.xlabel("No. of beds")
plt.ylabel("Square Ft.")
plt.show()

sleep = pd.read_csv('sleep_performance.csv')
# create your scatter plot here:
plt.scatter(x=sleep.hours_sleep,y=sleep.performance)
plt.xlabel("Hours Slept")
plt.ylabel("Performance")
plt.show()
# calculate the correlation for `hours_sleep` and `performance`:
corr_sleep_performance, p = pearsonr(sleep.hours_sleep,sleep.performance)
print(corr_sleep_performance)

#CORRELATIONS 2
npi = pd.read_csv("npi_sample.csv")
#contingency tables, frequency
special_authority_freq = pd.crosstab(npi.special,npi.authority)
print(special_authority_freq)

# save the table of proportions as special_authority_prop:
special_authority_prop = special_authority_freq/len(npi)  #can see where the majority of the responses lie helping to gauge possible correlations already  

# print out special_authority_prop
print(special_authority_prop)

# calculate and print authority_marginals
authority_marginals = special_authority_prop.sum(axis=0) #gets the proportions from the contingency table across the authority axis
print(authority_marginals)

# calculate and print special_marginals
special_marginals = special_authority_prop.sum(axis=1)
print(special_marginals)

special_authority_freq = pd.crosstab(npi.special, npi.authority)
print("observed contingency table:")
print(special_authority_freq)

from scipy.stats import chi2_contingency
# calculate the expected contingency table if there's no association and save it as expected
expected = chi2, pval, dof, expected = chi2_contingency(special_authority_freq)

# print out the expected frequency table
print("expected contingency table (no association):")
print(np.round(expected))

# calculate the chi squared statistic and save it as chi2, then print it:
chi2, pval, dof, expected = chi2_contingency(special_authority_freq)     #chi2 compares the actual and expected contingency tables
print(chi2)

