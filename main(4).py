import csv

empty_list = []
second_list = []
count = {}

#open Csv as file called csvfile and appends a list with each row of the source column

with open ('events.csv','r') as csvfile:
   reader = csv.DictReader(csvfile)
   for line in reader:
      empty_list.append(line['Source'])

#create another list called second_list that add each value only once 
for val in empty_list:
    if val in second_list:
        pass
    else:
        second_list.append(val)
#create a dictionary of each with the key as the name and the a value of 0 and then counts key and adds that count to the value
for item in second_list:
    count[item] = 0
    for t in empty_list:
        if t == item:
            count[item] +=1

#prints output of second list >>>>>> try to make this output better
print(second_list)

#ask's user to input name of one event by name
search = str(input("Please type prorgam you want to search event for? > "))

#prints the name of the program and the number of events the program counted
for keys,value in count.items():
    if search == keys:
        print(f'Program You Searched for {keys} had {value} Events Logged')