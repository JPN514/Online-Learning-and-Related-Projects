#Summarizing Automobile Evaluation Data

import pandas as pd
import numpy as np
car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())
print(len(car_eval))
# frequency for country:
country_freq = car_eval.manufacturer_country.value_counts()
print(country_freq,country_freq.index[-1])

# table of proportions:
country_prop = car_eval.manufacturer_country.value_counts(normalize=True)
print(country_prop)
# 22.8% manufactured in Japan

# all values of buying_cost category variable: 
print(car_eval.buying_cost.unique())

# convert buying_Cost as ordinal category:
value_list = ["low","med","high","vhigh"]
car_eval["buying_cost"] = pd.Categorical(
    car_eval["buying_cost"],
    value_list,
    ordered=True
)

# median buying cost:
median_buying_cost_num = np.median(car_eval.buying_cost.cat.codes)
print(median_buying_cost_num)
median_category = value_list[int(median_buying_cost_num)]
print(median_category)

# table of proportions for luggage: 
luggage_prop = car_eval.luggage.value_counts(normalize=True)
print(luggage_prop)

# luggage proportion table including all values:
luggage_prop = car_eval.luggage.value_counts(dropna=False,normalize=True)
print(luggage_prop) #no missing values as table is identical to table above

# replicate above without normalize parameter:
# use len to attain this
luggage_prop = car_eval.luggage.value_counts()/(len(car_eval))
print(luggage_prop)

# count of cars with 5 or more doors:
five_plus_doors = np.sum(car_eval.doors == "5more") 
print(five_plus_doors)

# proportion of cars with 5 or more doors:
print(five_plus_doors/len(car_eval))
