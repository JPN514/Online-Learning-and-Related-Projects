#DATA VISULAISATION FUNDAMENTALS:

import codecademylib
from matplotlib import pyplot as plt

#LINE CHARTS AND GRAPHS IN PYTHON:

#line graph:
days = [0,1,2,3,4,5,6]
money_spent = [10,12,12,10,14,22,24]
plt.plot(days,money_spent)
plt.show()

#another line grpah:
time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]
plt.plot(time,revenue)
plt.plot(time,costs)
plt.show()

plt.plot(time,revenue,color="purple",linestyle="--")
plt.plot(time,costs,color="#82edc9",marker="s")
plt.show()

#axis range:
x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)
plt.axis([0,12,2900,3100])
plt.xlabel("Time")
plt.ylabel("Dollars spent on coffee")
plt.title("My Last Twelve Years of Coffee Drinking")
plt.show()

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]
#subplots get plots in a grid style
plt.subplot(1,2,1) #1 row,2 columns, in position 1 ie on the left side here
plt.plot(months,temperature)
plt.subplot(1,2,2)
plt.plot(temperature,flights_to_hawaii,"o") #"o" makes a scatterplot
plt.show()

#adjusting the spacing between the subplots:
x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]
plt.subplot(2,1,1)
plt.plot(x,straight_line)
plt.subplot(2,2,3)
plt.plot(x,parabola)
plt.subplot(2,2,4)
plt.plot(x,cubic)
plt.subplots_adjust(wspace=0.35,bottom=0.2)
plt.show()

#Legend labels:
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]
legend_labels = ["Hyrule","Kakariko","Gerudo Valley"]
plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)
plt.legend(legend_labels,loc=8) #location 8 is lower centre,other locations are available.
plt.show()

#use ax as name for the subplot axes, helps if multiple axes are required in a subplot figure:
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)
ax = plt.subplot() #names the subplot ax, can refer to its properties by ax.property
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(["10%", "25%", "50%", "75%"])
plt.show()


#make a figure of (width,height) inches and save as a png
word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
plt.close("all") #closes all the currently open plots 
plt.plot(years,word_length)
plt.savefig("winning_word_lengths.png")
plt.figure(figsize=(7,3))
plt.plot(years,power_generated)
plt.savefig("power_generated.png")

#review with two lines on the same plot:
x = range(6)
y1 = [1, 2, 3, 4, 5, 6]
y2 = [-1, 1, 3, 4, 4, 4]
plt.plot(x, y1, marker='o', color='pink')
plt.plot(x, y2, marker='o', color='gray')
plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.legend(["Y1","Y2"], loc=4)
plt.show()


#DIFFERENT PLOT TYPES LESSON:::

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]
plt.bar(range(len(drinks)), sales)
#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
plt.show()


sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
#side by side bar chart
#Paste the x_values code here
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
x_values = [t*element + w*n for element
             in range(d)]
store1_x = x_values        
plt.bar(store1_x,sales1)  
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
x_values = [t*element + w*n for element
             in range(d)]
store2_x = x_values
plt.bar(store2_x,sales2)                
plt.show()

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
plt.bar(range(len(drinks)),sales1,label="Location 1")
plt.bar(range(len(drinks)),sales2,bottom=sales1,label="Location 2") #stacked bars 
plt.legend()
plt.show()


ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]
# Plot the bar graph here BAR WITH Y ERROR
plt.bar(range(len(drinks)),ounces_of_milk,yerr=error,capsize=5)
plt.show()

#ERROR SHADING ON A LINE GRAPH
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]
y_lower = [i - 0.1 * i for i in revenue]
y_upper = [i + 0.1 * i for i in revenue]
#your work here
plt.fill_between(range(len(months)),y_lower,y_upper,alpha=0.2) #alpha is the shading
plt.plot(range(len(months)),revenue)
ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
plt.show()

#BASIC PIE CHART
payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]
#make your pie chart here
plt.pie(payment_method_freqs)
plt.axis("equal") #stops the pie from looking too weird 
plt.show()

plt.pie(payment_method_freqs,labels=payment_method_names,autopct="%0.1f%%") #labels and percentage displayed
plt.axis('equal')
plt.legend()
plt.show()


from script import sales_times
#create the histogram here
plt.hist(sales_times,bins=20) #bins is the number of partitions in the data range 
plt.show()

from script import sales_times1
from script import sales_times2
plt.hist(sales_times1, bins=20,alpha=0.4,density=True)
#plot your other histogram here
plt.hist(sales_times2,bins=20,alpha=0.4,density=True)
plt.show() #alpha alters the transparency, allowing us to see each histgram more clearly. 
#density=True nomralises the histograms, ie will divide the column height by a constant to achieve total area of 1.


#RECREATE GRAPHS USING MATPLOTLIB LESSON :::

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

#PLOT 1
plt.figure(figsize=(10,8))
plt.bar(range(len(past_years_averages)),past_years_averages,yerr=error,capsize=5)
plt.axis([-0.5, 6.5, 70, 95])
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.title("Final Exam Averages")
plt.xlabel("Year")
plt.ylabel("Test average")
plt.savefig("my_bar_chart.png")
plt.show()


#PLOT 2 
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]
def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
# Make your chart here
school_a_x = create_x(2,0.8,1,5)
school_b_x = create_x(2,0.8,2,5)
plt.figure(figsize=(10,8))
plt.axis([0,10,70,90])
ax = plt.subplot()
plt.bar(school_a_x,middle_school_a,label="Middle School A")
plt.bar(school_b_x,middle_school_b,label="Middle School B")
middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.legend()
plt.title("Test Averages on Different Units")
plt.xlabel("Unit")
plt.ylabel("Test Average")
plt.savefig("my_side_by_side.png")
plt.show()


#PLOT 3:
import numpy as np
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom,Cs)
f_bottom = np.add(d_bottom,Ds)
#create your plot here
plt.figure(figsize=(10,8))
plt.bar(x,As,label="A")
plt.bar(x,Bs,bottom=As,label="B")
plt.bar(x,Cs,bottom=c_bottom,label="C")
plt.bar(x,Ds,bottom=d_bottom,label="D")
plt.bar(x,Fs,bottom=f_bottom,label="F")
ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.title("Grade Distribution")
plt.xlabel("Unit")
plt.ylabel("Number of Students")
plt.legend()
plt.savefig("my_stacked_bar.png")
plt.show()


#PLOT 4:
exam_scores1 = [62.58, 67.63, 81.37, 52.53, 62.98, 72.15, 59.05, 73.85, 97.24, 76.81, 89.34, 74.44, 68.52, 85.13, 90.75, 70.29, 75.62, 85.38, 77.82, 98.31, 79.08, 61.72, 71.33, 80.77, 80.31, 78.16, 61.15, 64.99, 72.67, 78.94]
exam_scores2 = [72.38, 71.28, 79.24, 83.86, 84.42, 79.38, 75.51, 76.63, 81.48,78.81,79.23,74.38,79.27,81.07,75.42,90.35,82.93,86.74,81.33,95.1,86.57,83.66,85.58,81.87,92.14,72.15,91.64,74.21,89.04,76.54,81.9,96.5,80.05,74.77,72.26,73.23,92.6,66.22,70.09,77.2]

# Make your plot here
plt.figure(figsize=(10,8))
plt.hist(exam_scores1,bins=12,density=True,histtype = 'step',linewidth=2,label="1st Yr Teaching")
plt.hist(exam_scores2,bins=12,density=True,histtype = 'step',linewidth=2,label="2nd Yr Teaching")
plt.legend()
plt.xlabel("Percentage")
plt.ylabel("Frequency")
plt.title("Final Exam Score Distribution")
plt.savefig("my_histogram.png")
plt.show()


#PLOT 5:
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]
#Make your plot here
plt.figure(figsize=(10,8))
plt.pie(num_hardest_reported,labels=unit_topics,autopct="%1d%%")
plt.axis("equal")
plt.title("Hardest Topics")
plt.savefig("my_pie_chart.png")
plt.show()


#PLOT 6:
hours_reported =[3, 2.5, 2.75, 2.5, 2.75, 3.0, 3.5, 3.25, 3.25,  3.5, 3.5, 3.75, 3.75,4, 4.0, 3.75,  4.0, 4.25, 4.25, 4.5, 4.5, 5.0, 5.25, 5, 5.25, 5.5, 5.5, 5.75, 5.25, 4.75]
exam_scores = [52.53, 59.05, 61.15, 61.72, 62.58, 62.98, 64.99, 67.63, 68.52, 70.29, 71.33, 72.15, 72.67, 73.85, 74.44, 75.62, 76.81, 77.82, 78.16, 78.94, 79.08, 80.31, 80.77, 81.37, 85.13, 85.38, 89.34, 90.75, 97.24, 98.31]
# Create your figure here
plt.figure(figsize=(10,8))
plt.plot(exam_scores,hours_reported,linewidth=2)
# Create your hours_lower_bound and hours_upper_bound lists here 
hours_lower_bound = [hours - (hours*0.2) for hours in hours_reported]
hours_upper_bound = [hours + (hours*0.2) for hours in hours_reported]
# Make your graph here
plt.fill_between(exam_scores,hours_lower_bound,hours_upper_bound,alpha=0.2)
plt.title("Time spent studying vs final exam scores")
plt.xlabel("Score")
plt.ylabel("Hours studying (self-reported)")
plt.savefig("my_line_graph.png")
plt.show()


#NEXT LESSON
#VISUALISING CATEGORICAL DATA ::::
import pandas as pd
import seaborn as sns
df = pd.read_csv("school_data.csv")
print(df.head())

value_order = ["NOT ENOUGH DATA", "VERY WEAK", "WEAK", "NEUTRAL", "STRONG", "VERY STRONG"]
type_of_data = "ordinal"
# plot using .countplot() method here
sns.countplot(df["Supportive Environment"],order=value_order) #uses the order above to order the bars on the bar chart
plt.xticks(rotation=30)
plt.show()

# show your plot here

water_usage = pd.read_csv("water_usage.csv")
print(water_usage.head())
wedge_sizes = water_usage.prop
pie_labels = water_usage.water_source

plt.pie(wedge_sizes,labels=pie_labels)
plt.axis("equal")
plt.title("Distribution of House Water Usage")
plt.show()

#Side by side pie charts, one easier to read than the other
major_data = pd.read_csv("major_data.csv")
print(major_data.head())
major_data_agg = pd.read_csv("major_data_agg.csv")
print(major_data_agg.head())

pie_wedges = major_data["proportion"]
pie_labels = major_data["major"]

pie_wedges_agg = major_data_agg["proportion"]
pie_labels_agg = major_data_agg["department"]

plt.subplot(2,1,1)
plt.pie(pie_wedges, labels = pie_labels)
plt.axis('Equal')
plt.title("Too Many Slices")
plt.tight_layout()

plt.subplot(2,1,2)
plt.pie(pie_wedges_agg,labels=pie_labels_agg)
plt.axis('Equal')
plt.title("Good Number of Slices")
plt.tight_layout()

plt.show()

