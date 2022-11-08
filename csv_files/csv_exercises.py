import csv
#  import not working. Why? Code works though seems hooked up. 
##################### CSV #####################

################## Q1 ################## ✅
# Write a program that reads in colours_20_simple.csv and output the colour data.
# Input: colours_20.csv
# Output: Contents of the colours_20_simple.csv file, in order of questions direction
# import csv

# q_one = open('colours_20_simple.csv', mode='r')
# print(q_one.read())
# q_one.close()
 
################## Q2 ################## ✅
# Write a program that reads in colours_20_simple.csv
# and outputs the colour data in order English, Hexthen (Hex) RGB.
# Input: colours_20_simple.csv
# 1.
# q_two = open('colours_20_simple.csv', mode='r')
# print(q_two.read())
# q_two.close()

# order: English, Hexthen RGB
# q_two = open('colours_20_simple.csv', mode='r')
# with open('colours_20_simple.csv') as file_object:
#     print(file_object)
# q_two.close()

# q_two = colours_20_simple.csv("data.csv")
# print(q_two)

# import csv

# with open("colours_20_simple.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(f'{line[2]:<20}', f'{line[1]:<20}', f'{line[0]:<20}')


################## Q3 ################## ✅
# Write a program that reads incolours_20.csvand output the colour data in order English, Hex then RGB
# Input: colours_20.csv
# import csv

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(f'{line[4]:<20}', f'{line[2]:<20}', f'{line[1]:<20}')

################## Q4 ##################
# Using the same colour csv files, 
# write a program that outputs the number of times each
# of the following colours appear in the English Name:

# Input: colours_213.csv
# Expected output:
# Red: 21
# Green: 30
# Blue: 25
# Yellow: 19

import csv

def colour_finder(reader, colour):
    count = 0
    for line in reader:
        if colour in line[4].lower():
            count += 1
    return(count)

with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    print(colour_finder(reader, "yellow"))
    #for line in reader(line.lower()):

    #print(f'Red: {colour_finder(reader, "red")}', f'Green: {colour_finder(reader, "Green")}', f'Blue: {colour_finder(reader, "Blue")}', f'Yellow: {colour_finder(reader, "Yellow")}')



##### Pt. 1 #####
# import csv

# def colour_finder(reader, colour):
#     count = 0
#     for line in reader:
#         for word in line:
#             if colour in word:
#                 count += 1
#     return(count)

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     print(f'Red: {colour_finder(reader, "red")}', f'Green: {colour_finder(reader, "Green")}', f'Blue: {colour_finder(reader, "Blue")}', f'Yellow: {colour_finder(reader, "Yellow")}')

# or: 
#     print(f'Red: {colour_finder(reader, "red")}')
#     print(f'Green: {colour_finder(reader, "green")}'),
#     print(f'Blue: {colour_finder(reader, "blue")}'),
#     print(f'Yellow: {colour_finder(reader, "yellow")}')


import csv

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)

# def colour_finder(colour):
#     count = 0
#     for line in reader:
#         for word in line:
#             if colour in word:
#                 count += 1
#     return(count)


################## Q5 ##################
# galaxies.py contains data about 82 different galaxies and their velocities(km/sec).
# Using this data, output the galaxy with the slowest velocity,
# and the galaxy with the highest velocity.

# Input: galaxies.csv
# Output: 
# Galaxy 1 has the min velocity of 9172km/sec.
# Galaxy 82 has the max velocity of 34279km/sec.
