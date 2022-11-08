########### Q2 ###########
# import csv
# colours_list = []
# with open("colours_20_simple.csv") as colours_csv:
#     colours_csv_reader = csv.reader(colours_csv)
#     header = next(colours_csv_reader)
#     casted_colours_list = list(colours_csv_reader)
#     # for row in colours_csv_reader:
#         # print(f'{row[2]}, Hex: {row[1]}, RGB: {row[2]}') # this as option / example1 without the empty array above, nor the two lines following below this line. 
# #         colours_list.append(row)
# # print(colours_list) # option2 excluding previous print, including empty aray variable above and excluding line below. 
# print(casted_colours_list) # option excluding the for row in xxx and with an added variable of matching name 


########### Q4 ###########
### Pt 1
# red_counter = 0
# green_counter = 0
# blue_counter = 0
# yellow_counter = 0
# import csv
# with open("colours_20.csv") as colours_counter:
#     reader = csv.reader(colours_csv)
#     for row in reader:
#         if "red" in row[4]:
#             red_counter += 1
#         elif "green" in row[4]:
#             green_counter += 1
#         elif "blue" in row[4]:
#             blue_counter += 1
#         elif "yellow" in row[4]:
#             yellow_counter =+ 1
# print(f"Red: { red_counter}")
# print(f"Green: { green_counter}")
# print(f"Blue: { blue_counter}")
# print(f"Yellow: { yellow_counter}")
            

########### Q5 ###########
import csv 

max_velocity = 0
min_velocity = 999999999
min_galaxy = ''
max_galaxy = ''

with open("galaxies.csv") as galaxies_csv:
    reader = csv.reader(galaxies_csv)
    next(galaxies_csv)
    for row in reader:
#        print(f"current value of {max_velocity}") # this used after writing this out, as a way to show what has been happening/ break it apart as explanation to the class. 
        if row[1] > max_velocity:
            max_velocity = int(row[1])
            max_velocity = row[0]
        elif row[1] < min_velocity:
            min_velocity = int(row[1])
            min_velocity = row[0]
print(f"Galaxy {min_galaxy[0]} has the min velocity of {min_velocity[1]}km/sec.")
print(f"Galaxy {max_galaxy[0]} has the max velocity of {max_velocity[1]}km/sec.")
