# Roller Coaster project 

# data visulaisations for various metrics relating to roller coasters

import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
wood = pd.read_csv("Golden_Ticket_Award_Winners_Wood.csv")
steel = pd.read_csv("Golden_Ticket_Award_Winners_Steel.csv")
print(wood.head())
print(steel.head())

# write function to plot rankings over time for 1 roller coaster here:
def rank_coaster(name,park,df):
  ranking = df[(df.Name == name) & (df.Park == park)]
  plt.plot(ranking["Year of Rank"],ranking.Points)
  plt.title("Roller Coaster Ranking Points Over Time")
  plt.xlabel("Year")
  plt.ylabel("Points")
  plt.show()

plt.clf()
rank_coaster("El Toro","Six Flags Great Adventure",wood)

# write function to plot rankings over time for 2 roller coasters here:
def two_rank_coaster(name1,park1,name2,park2,df):
  ranking1 = df[(df.Name == name1) & (df.Park == park1)]
  ranking2 = df[(df.Name == name2) & (df.Park == park2)]
  legend_labels = [name1,name2]
  plt.plot(ranking1["Year of Rank"],ranking1.Points)
  plt.plot(ranking2["Year of Rank"],ranking2.Points)
  plt.title("Roller Coaster Ranking Points Over Time")
  plt.xlabel("Year")
  plt.ylabel("Points")
  plt.legend(legend_labels)
  plt.show()
plt.clf()

two_rank_coaster("El Toro","Six Flags Great Adventure","Boulder Dash","Lake Compounce",wood)
plt.clf()

# write function to plot top n rankings over time here:
def top_n(n,df):
  top = df[df["Rank"] <= n]
  fig, ax = plt.subplots(figsize=(10,10))
  for coaster in set(top["Name"]):
    coaster_rankings = top[top["Name"] == coaster]
    ax.plot(coaster_rankings["Year of Rank"],coaster_rankings["Rank"],label=coaster)
  ax.set_yticks([i for i in range(1,6)])
  plt.title("Top 10 Rankings")
  plt.xlabel("Year")
  plt.ylabel("Ranking")
  plt.legend(loc=1)
  plt.show()

plt.clf()
top_n(5,wood)

# load roller coaster data here:
coasters = pd.read_csv("roller_coasters.csv")
print(coasters.head())

# write function to plot histogram of column values here:
def coaster_hist(df,column):
  plt.hist(df[column])
  legend = [column]
  plt.legend(legend)
  plt.xlabel(column)
  plt.ylabel("Number of Roller Coasters")
  plt.show()

#coaster_hist(coasters,"speed")
plt.clf()

# write function to plot inversions by coaster at a park here:
def inversions(df,park):
  park_df = df[df["park"] == park]
  roller_coaster = park_df["name"]
  inversions = park_df["num_inversions"]
  plt.figure(figsize = (20, 15))
  ax = plt.subplot()
  ay = plt.subplot()
  plt.bar(range(len(roller_coaster)), inversions)
  ax.set_xticks(range(len(roller_coaster)))
  ax.set_xticklabels(roller_coaster)
  plt.xticks(rotation=45)
  plt.legend([park])
  plt.show()

inversions(coasters, "Dollywood")
plt.clf()
    
# write function to plot pie chart of operating status here:
def pie(coasters):
  df_operating = coasters[coasters["status"] == "status.operating"]
  df_closed = coasters[coasters["status"] == "status.closed.definitely"]
  count = [len(df_operating), len(df_closed)]
  labelsdata = ["Operating", "Closed"]
  plt.pie(count, autopct="%0.1f%%", labels = labelsdata)
  plt.axis("equal")
  plt.show()

pie(coasters)
plt.clf()
  
# write function to create scatter plot of any two numeric columns here:
def scatter(df,column1,column2):
  c1 = df[column1]
  c2 = df[column2]
  x = range(len(df))
  plt.figure(figsize=(20, 20))
  ax = plt.subplot()
  plt.scatter(x, c1, color= "blue", alpha= 0.5)
  plt.scatter(x, c2, color= "green", alpha=0.5)
  ax.set_xlabel("Variables")
  ax.set_ylabel("Roller Coasters")
  plt.ylim(0, 200)
  plt.legend([column1, column2])
  plt.show()

scatter(coasters, "speed", "height")
plt.clf()