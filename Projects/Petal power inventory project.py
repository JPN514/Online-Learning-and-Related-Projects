#Petal power inventory project


import pandas as pd 
inventory = pd.read_csv("inventory.csv")
print(inventory[:10])
staten_island = inventory[:10]
product_request = staten_island["product_description"]

seed_request = inventory[(inventory["location"]=="Brooklyn") & (inventory["product_type"]=="seeds")]

mylambda = lambda row : "True" if row["quantity"] > 0 else "False"
inventory["in_stock"] = inventory.apply(mylambda,axis=1)
print(inventory)

inventory["total_value"] = inventory.apply(lambda row :
row["price"]*row["quantity"],axis=1)
print(inventory)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory["full_description"] = inventory.apply(combine_lambda,axis=1)
print(inventory)
