################## Q3 ##################
# Write a program that reads in colours_20.csv and output the colour data in order English, Hex then RGB
# Input: colours_20.csv
# Output: 

import csv

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(f'{line[2]:<20}', f'{line[1]:<20}', f'{line[0]:<20}')