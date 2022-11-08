import csv

def colour_finder(reader, colour):
    count = 0
    for line in reader:
        if colour in line[4].lower():
            count += 1
    return(count)

with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    print(colour_finder(reader, "Red"))
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