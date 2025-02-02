import csv
import matplotlib.pyplot as plt
import numpy as np


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

count.pop(None)

#prints output of second list >>>>>> try to make this output better
print(second_list)

#ask's user to input name of one event by name
print('')
search = str(input(" PLEASE INPUT THE PROGRAM NAME YOU WANT TO SEARCH FOR ?> "))

#prints the name of the program and the number of events the program counted
for keys,value in count.items():
    if search == keys:
        print(f'Program {keys} had {value} Events Logged')

dansdict = count

names = list(dansdict.keys())
Age = list(dansdict.values())

key_to_change = search
index_to_chnage = names.index(key_to_change)

plt.figure(figsize=(16,9))
bars = plt.bar(names,Age, color='blue')
bars[index_to_chnage].set_color('red')
plt.ylabel('Events Over Time')
plt.xticks(rotation = 90)
plt.xticks(size=8)
plt.ylim(0, 1000)
# Save the plot to a file


plt.savefig('plot.png')  # Saves the plot as a PNG file

