#A/B testing for flyshoe.com

import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

views_by_source = ad_clicks.groupby("utm_source").user_id.count().reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(["utm_source","is_click"]).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns = "is_click", index = "utm_source", values = "user_id").reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])
print(clicks_pivot)    

group_by_ads = ad_clicks.groupby("experimental_group").user_id.count().reset_index()

print(group_by_ads)

percentage_ads_clicked = ad_clicks.groupby(["experimental_group","is_click"]).user_id.count().reset_index()
print(percentage_ads_clicked)
pivot_percentage_ads_clicked = \
percentage_ads_clicked.pivot(columns = "is_click", index = "experimental_group", values = "user_id").reset_index()
print(pivot_percentage_ads_clicked)
pivot_percentage_ads_clicked["percent clicked"] = \
pivot_percentage_ads_clicked[True] / (pivot_percentage_ads_clicked[True]+pivot_percentage_ads_clicked[False])
print(pivot_percentage_ads_clicked)

a_clicks = ad_clicks[ad_clicks["experimental_group"] == "A"]
b_clicks = ad_clicks[ad_clicks["experimental_group"] == "B"]
a_clicks_day = a_clicks.groupby(["is_click", "day"]).user_id.count().reset_index()
a_clicks_day_pivot = a_clicks_day.pivot(columns = "is_click", index = "day", values = "user_id").reset_index()
b_clicks_day = b_clicks.groupby(["is_click", "day"]).user_id.count().reset_index()
b_clicks_day_pivot = b_clicks_day.pivot(columns = "is_click", index = "day", values = "user_id").reset_index()
a_clicks_day_pivot["percent_clicked"] = \
a_clicks_day_pivot[True] / \
(a_clicks_day_pivot[True] + a_clicks_day_pivot[False])
b_clicks_day_pivot["percent_clicked"] = \
b_clicks_day_pivot[True] / \
(b_clicks_day_pivot[True] + b_clicks_day_pivot[False])
print(a_clicks_day_pivot)
print(b_clicks_day_pivot)

