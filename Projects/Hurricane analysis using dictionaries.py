#Hurricane analysis using dictionaries

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def update_damages(damages):
  conversion = {"M": 1000000,
              "B": 1000000000}
  new_damages = []
  for item in damages:
    if item == "Damages not recorded":
      new_damages.append(item)
    elif item[-1] in conversion.keys():
      new_damage = float(item[:-1]) * conversion[item[-1]]
      new_damages.append(new_damage)
    #print(new_damages)  
  return new_damages

# test function by updating damages
damages_updated = update_damages(damages)
print(damages_updated)

# 2 
# Create a Table
table = []
for i in range(0,34):
  hurricane = {"Name": names[i],
 "Month": months[i],
 "Year": years[i],
 "Max Sustained Wind": max_sustained_winds[i],
 "Areas Affected": areas_affected[i],
 "Damage": damages_updated[i],
 "Deaths": deaths[i]}
  table.append(hurricane)
# Create and view the hurricanes dictionary
hurricanes = {}
for hurricane in table:
  hurricanes[hurricane["Name"]] = hurricane

print(hurricanes)

# 3
# Organizing by Year
def year_order(hurricanes):
  year_hurricanes = {} 
# create a new dictionary of hurricanes with year and key
  for hurricane in hurricanes:
    year = hurricanes[hurricane]["Year"]
    if year in year_hurricanes.keys():
      year_hurricanes[year].append(hurricane) 
    else:
      year_hurricanes[year] = [hurricane]  
  return year_hurricanes

year_hurricanes = year_order(hurricanes)
print(year_hurricanes)    

# 4
# Counting Damaged Areas
def count_areas(hurricanes):
# create dictionary of areas to store the number of hurricanes involved in
  areas = {}
  for hurricane in hurricanes:
    for area in hurricanes[hurricane]["Areas Affected"]:
      if area in areas:
        count = count + 1
        areas[area] = count
      else:
        count = 1
        areas[area] = count
  return(areas)

print(count_areas(hurricanes))
affected_areas_count = count_areas(hurricanes)


# 5 
# Calculating Maximum Hurricane Count
def calc_max(areas):
# find most frequently affected area and the number of hurricanes involved in 
  values = sorted(areas.values())
  max_value = values[-1]
  max_affected = {} 
  for area in areas:
    if areas[area] == max_value:
      max_affected[area] = max_value
  return(max_affected)

print(calc_max(affected_areas_count))

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def most_deaths(hurricanes):
  deaths.sort(reverse=True)
  most_deaths = deaths[0]
  max_deaths_canes = {}
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Deaths"] == most_deaths:
      max_deaths_canes[hurricane] = most_deaths
  return max_deaths_canes

print(most_deaths(hurricanes))      

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def mortality_rating(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  mortality_canes = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Deaths"] == 0:
      mortality_canes[0].append(hurricane)
    elif hurricanes[hurricane]["Deaths"] <= 100:
      mortality_canes[1].append(hurricane)
    elif hurricanes[hurricane]["Deaths"] <= 500:
      mortality_canes[2].append(hurricane)
    elif hurricanes[hurricane]["Deaths"] <= 1000:
      mortality_canes[3].append(hurricane)
    elif hurricanes[hurricane]["Deaths"] <= 10000:
      mortality_canes[4].append(hurricane)
    else:
      mortality_canes[5].append(hurricane)  

  return mortality_canes

print(mortality_rating(hurricanes))    



# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def max_damages(hurricanes):
  new_damages = []
  for damage in damages_updated:
    if isinstance(damage,str) == True:
      damage = 0 
      new_damages.append(float(damage))
    else: 
      damage = float(damage)
      new_damages.append(damage)
  print(new_damages)  
  new_damages.sort(reverse=True)
  max_value = new_damages[0]
  print(max_value)
  max_damage_cane = {}
  for hurricane in hurricanes:
    if isinstance(hurricanes[hurricane]["Damage"],str) == True:
      pass
    else:  
      if float(hurricanes[hurricane]["Damage"]) == max_value:
        max_damage_cane[hurricane] = max_value

  print("Hurricane {} caused the most damages at a cost of {}. ".format(max_damage_cane,max_value))   

max_damages(hurricanes)


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def by_damage(hurricanes):
  for hurricane in hurricanes:
    if isinstance(hurricanes[hurricane]["Damage"],str) == True:
      hurricanes[hurricane]["Damage"] = 0

  damages_canes = {0:[],1:[],2:[],3:[],4:[],5:[]}
  
  for hurricane in hurricanes:
    if hurricanes[hurricane]["Damage"] == 0:
      damages_canes[0].append(hurricane)
    elif hurricanes[hurricane]["Damage"] <= damage_scale[1]:
      damages_canes[1].append(hurricane)
    elif hurricanes[hurricane]["Damage"] <= damage_scale[2]:
      damages_canes[2].append(hurricane)
    elif hurricanes[hurricane]["Damage"] <= damage_scale[3]:
      damages_canes[3].append(hurricane)
    elif hurricanes[hurricane]["Damage"] <= damage_scale[4]:
      damages_canes[4].append(hurricane)
    else:
      damages_canes[5].append(hurricane)  

    print(damages_canes)  

by_damage(hurricanes)