#NBA TRENDS
#correlations between nba data and seasons

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

#knicks and nets points scored by game 2010:
knicks_pts_10 = nba_2010.pts[nba_2010["fran_id"]=="Knicks"]
nets_pts_10 = nba_2010.pts[nba.fran_id=="Nets"]

#difference in mean points scored 2010:
diff_points = knicks_pts_10.mean() - nets_pts_10.mean()
print(diff_points)

#Overlapping histogram comparing points scored 2010:
plt.hist(knicks_pts_10, color="blue", label="Knicks pts",normed=True,alpha=0.5)
plt.hist(nets_pts_10, color="red", label="Nets_pts",normed=True,alpha=0.5)
plt.legend()
plt.title("2010 season")
plt.show()
plt.close()

#Doing the same for the 2014 season:
#knicks and nets points scored by game 2014:
knicks_pts_14 = nba_2014.pts[nba_2014["fran_id"]=="Knicks"]
nets_pts_14 = nba_2014.pts[nba.fran_id=="Nets"]

#difference in mean points scored:
diff_points = knicks_pts_14.mean() - nets_pts_14.mean()
print(diff_points)

#Overlapping histogram comparing points scored
plt.hist(knicks_pts_14, color="blue", label="Knicks pts",normed=True,alpha=0.5)
plt.hist(nets_pts_14, color="red", label="Nets_pts",normed=True,alpha=0.5)
plt.legend()
plt.title("2014 season")
plt.show()
plt.close() 

#2010 boxplot of points scored by franchise:
sns.boxplot(data=nba_2010,x="fran_id",y="pts")
plt.title("points by team")
plt.xlabel("Franchise")
plt.ylabel("Points")
plt.legend()
plt.show()
plt.close()

#contingency table for winning at home vs away:
location_result_freq = pd.crosstab(nba_2010.game_result,nba_2010.game_location)
print(location_result_freq) #seemingly win more at home and lose more away
#proportions table:
location_result_proportions = location_result_freq / len(nba_2010)
print(location_result_proportions)

#chi2 for the expected contingency table:
expected = chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)

#covariance of forecast (prob. of winning) and points diff (essentially win or loss):
points_diff_forecast_cov = np.cov(nba_2010.point_diff,nba_2010.forecast)
print(points_diff_forecast_cov) #1.37 covariance

#calculate the correlation between forecast and points diff:
point_diff_forecast_corr, p = pearsonr(nba_2010.point_diff,nba_2010.forecast)
print(point_diff_forecast_corr)

#Scatter plot of forecast and points difference:
plt.scatter(x=nba_2010.forecast,y=nba_2010.point_diff)
plt.title("Forecast vs point difference")
plt.xlabel("Forecast")
plt.ylabel("Points Difference")
plt.legend()
plt.show()
plt.close()
