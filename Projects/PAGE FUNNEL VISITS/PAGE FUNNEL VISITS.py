#PAGE FUNNEL VISITS 
#pd merges 

import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())         

visits_cart_left = pd.merge(visits,cart,how="left")
print(visits_cart_left)
print(visits_cart_left.user_id.count())
null_cart = visits_cart_left[visits_cart_left.cart_time.isnull()] #frame with all the null carts
print(null_cart.user_id.count())
no_cart_percent = float(null_cart.user_id.count()) / float(visits_cart_left.user_id.count())
print(no_cart_percent)
print(1652/len(visits_cart_left))

cart_checkout_left = pd.merge(cart,checkout,how="left")
print(cart_checkout_left)
null_checkout = cart_checkout_left[cart_checkout_left.checkout_time.isnull()] #everyone who didnt checkout 
no_checkout_percent = float(null_checkout.user_id.count()) / float(cart_checkout_left.user_id.count())
print(no_checkout_percent)

#what percent proceeded to checkout but didnt buy a shirt
all_data = visits.merge(cart,how="left").merge(checkout,how="left").merge(purchase,how="left")
print(all_data)

checkout_yes = all_data[all_data.checkout_time.isnull() == False] #everyone who went to checkout
print(checkout_yes)
purchase_no = checkout_yes[checkout_yes.purchase_time.isnull()] #everyone who didnt purchase
checkout_yes_count = len(checkout_yes)
purchase_no_count = purchase_no.user_id.count()
no_buy_percent = float(purchase_no_count) / \
float(checkout_yes_count)
print(no_buy_percent)

print(no_cart_percent) #weakest is visit to cart
print(no_checkout_percent)
print(no_buy_percent)

#average time from visit to purchase
all_data["time_spent"] = all_data["purchase_time"] - all_data["visit_time"]
print(all_data.time_spent.mean())
