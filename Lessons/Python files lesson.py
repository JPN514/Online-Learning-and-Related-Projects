#Python files lesson 

#MAY NOT RUN 

#files in python

with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)  

#open and read the lines plus printout 
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():   #readlines reads through all the lines in the file
    print(line)
    

with open('just_the_first.txt') as first_line_doc: 
  first_line = first_line_doc.readline()  #reads just one line at a time
print(first_line)     

#writes to the file 
with open('bad_bands.txt','w') as bad_bands_doc:
   bad_bands_doc.write("SWS") 
   
#writes (appends) to the file without deleting stuff plus moves to the next line
with open("cool_dogs.txt",'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy\n')
  
  
with open('fun_file.txt') as close_this_file:
  setup = close_this_file.readline()
  punchline = close_this_file.readline()
print(setup)  

with open('logger.csv') as log_csv_file:
  logs = log_csv_file.read()
  print(logs)  
  
import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)  #dict reader allows us to convert the lines of csv file to dictionaries with the first row of csv file as the keys 
  for row in cool_csv_dict:
    print(row['Cool Fact'])   #this prints each entry in the cool fact column 
    
import csv
with open('books.csv',newline='') as books_csv:
  books_reader = csv.DictReader(books_csv,delimiter='@')  #delimiter sets the character that separates the file e.g. a ',' or '@' 
  isbn_list = []
  for row in books_reader:
    isbn_list.append(row['ISBN'])   #reads the ISBN entry in each row of the file
  print(isbn_list)  


#below writes the access log to a csv file after setting up the headers of the file  
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']
import csv

with open('logger.csv','w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv,fieldnames=fields)

  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)
    
#opens and prints a json file
import json 
with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])


#below the dump file writes data_payload to the target json file, in this case data_json
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]
import json
 
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)


