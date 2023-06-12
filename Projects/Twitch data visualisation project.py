# Twitch data visualisation project
# Python data visualisations for twitch streaming data
# bar chart, pie chart and time series 


import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

# 2,3,4. games and viewers bar chart:
plt.bar((range(len(games))),viewers,color='green')
ax = plt.subplot()
plt.title("Number of viewers per game")
plt.legend(["Twitch"])
plt.xlabel("Game")
plt.ylabel("Viewers")
ax.set_xticks(range(len(games)))
ax.set_xticklabels(games,rotation=30)
plt.show()
plt.clf()

# 5,6. pie chart of countries of viewers:
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen'] # to help with the colour scheme

plt.pie(countries,labels = labels,colors=colors)
plt.title("Countries of viewers")
plt.axis("equal")
plt.show()
plt.clf()

# 7 explode the US portion:
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(countries, explode=explode, colors=colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title("League of Legends Viewers' Whereabouts")
plt.legend(labels, loc="right")
plt.show()
plt.clf()


# 9,10. line graph of viewers:
plt.plot(hour,viewers_hour)
plt.title("Number of viewers per hour of the day")
plt.xlabel("Hour")
plt.ylabel("Viewers")
plt.legend(['2015-01-01'])
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])
plt.show()
plt.clf()

# 11. account for the error margin in the time series above:
y_upper = [i + (i*0.15) for i in viewers_hour]
y_lower = [i - (i*0.15) for i in viewers_hour]

plt.plot(hour,viewers_hour,color='green')
plt.title("Number of viewers per hour of the day(15% error)")
plt.xlabel("Hour")
plt.ylabel("Viewers")
plt.legend(['2015-01-01'])
ax = plt.subplot()
ax.set_xticks(hour)
ax.set_yticks([0, 20, 40, 60, 80, 100, 120])
plt.fill_between(hour, y_lower, y_upper, alpha=0.2)
plt.show()
plt.clf()