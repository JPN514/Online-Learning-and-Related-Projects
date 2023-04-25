import requests
import csv
import pandas
import numpy

#OVERVIEW OF DATA ACQUISITION 

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36') 

r_text = r.text
# Access data as JSON string
print(r.text)
r_json = r.json()
# Access decoded JSON data as Python object
print(r_json)

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

r_json = r.json()

with open('commute_data.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r.json())
  
commute_df = pandas.read_csv("commute_data.csv")
commute_df.columns = ['name', 'total_commuters', 'over 90mins','state','county']
print(commute_df.head())

print(numpy.random.binomial(n=1,p=0.8,size=500))
print(numpy.random.binomial(n=100,p=0.8,size=500))

first_name = "Jake"
last_name = "North"
def password_generator(first_name,last_name):
  password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return password

temp_password = password_generator(first_name,last_name)
print(temp_password)

def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password


poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title,poem_title_fixed)
poem_author_fixed = poem_author.upper()
print(poem_author,poem_author_fixed)

line_one = "The sky has given over"
line_one_words = line_one.split(" ")

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1]) 
print(author_last_names)

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""
spring_storm_lines = spring_storm_text.split("\n") #splits into the lines 

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words) #joins the items of the list in a string with a space inbetween each item 

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = "\n".join(winter_trees_lines) #joins the strings together with a newline each time
print(winter_trees_full)

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
   love_maybe_lines_stripped.append(line.strip())    #strip removes the spaces(in this specific case) from each item in the list
love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace("Tomer","Toomer") #replaces each instance of the first substring with the second substring in the target string toomer_bio

god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown") #find returns the index of the first letter of the substring, here 'd', at position 20
print(disown_placement) 

def poem_title_card(title, poet):
    poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
    return poem_desc

def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc

my_beard_description = poem_description(author = "Shel Silverstein",title = "My Beard",original_work = "Where the Sidewalk Ends",publishing_date = "1974")


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  
# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
    
#dictionaries below:    
translations = {"mountain":"orod","bread":"bass","friend":"mellon","horse":"roch"}

children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"], "Corleone":["Sonny", "Fredo", "Michael"]}

animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12 #adds the value 12 to the key "monkeys"
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper":138475,"stringQueen":85739}) #adds the keys/value pairs to the dictionary
print(user_ids)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress":"Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks,caffeine) #zip combines elements of two lists into tuples e.g (espresso,64)
drinks_to_caffeine = {key:value for key,value in zipped_drinks}

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {song:plays for song,plays in zip(songs,playcounts)}
print(plays)
plays.update({"Purple Haze":1})
plays["Respect"] = 94
library = {"The Best Songs":plays,"Sunday Feelings":{}}
print(library)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

zodiac_elements["energy"] = "Not a Zodiac element"
key_to_check = "energy"                            #key checker
if key_to_check in zodiac_elements:
  print(zodiac_elements["energy"])

#get searches the dict for the key and returns its value if it exists and None if not
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder")
print(tc_id)
stack_id = user_ids.get("superStackSmash",100000) #the second value will be returned if the key is not present in the dictionary
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains",0) #pop returns the value of the key in the dict then removes this key/value pair from the dict
health_points += available_items.pop("power stew",0)
health_points += available_items.pop("mystic bread",0)
print(available_items)
print(health_points)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
lessons = num_exercises.keys() #returns a list of the keys of the dict 
print(users)
print(lessons)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for score in num_exercises.values():   #gets the values of the dict in a list
  total_exercises += score
print(total_exercises)  

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for job,percent in pct_women_in_occupation.items():
  print("Women make up {} percent of {}s.".format(percent,job))  #items returns a tuple (key,value) for each pair in the list
  
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}
spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)
for key,value in spread.items():
  print("Your {} is the {} card.".format(key,value))
  




