# #  galaxies.py contains data about 82 different galaxies and their velocities(km/sec).
# # Using this data, output the galaxy with the slowest velocity,
# # and the galaxy with the highest velocity.
# # Input: galaxies.csv
# # Expected output: 
# # Galaxy 1 has the min velocity of 9172km/sec.
# # Galaxy 82 has the max velocity of 34279km/sec.

# import csv 

# with open("galaxies.csv") as csv_file:

#     maxvelocity = 0
#     data = csv_file.readlines

#     for line in csv_file:
#         linelist = line.split(",")
#         galaxy = linelist[0]
#         velocity = linelist[1]
#         for x in 
#     reader = csv.reader(csv_file)
#     print(max(reader))
# import csv
# def find_velocity(reader, velocity):
#     count = 0
#     for line in reader:
#         if velocity in line[1]:
#             count += 1
#     return(count)
# with open("colours_213.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     print(colour_finder(reader, "yellow"))
# to get a list, instead of a generator, use
# xy = list(read_lines())
# print(f'Galaxy {} has the min velocity of {}')
# print(f'Galaxy {} has the min velocity of {}')

######## This one works!! ########
# import csv 

# with open("galaxies.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     data = list(reader)
    # count = 0
    # galaxy_max = []
    # galaxy_min = []
    # for galaxy in data[1:]:
    #     if count < int(galaxy[1]):
    #         count = int(galaxy[1])
    #         galaxy_max = galaxy
    # for galaxy in data[1:]:
    #     if count > int(galaxy[1]):
    #         count = int(galaxy[1])
    #         galaxy_min = galaxy
    # print(f"Galaxy {galaxy_max[0]} has the max velocity of {galaxy_max[1]}km/sec.")
    # print(f"Galaxy {galaxy_min[0]} has the min velocity of {galaxy_min[1]}km/sec.")


import csv 

def get_velocity(galaxy):
    return int(galaxy[1])

with open("galaxies.csv") as csv_file:
    reader = csv.reader(csv_file)
    data = list(reader)[1:]
    data.sort(key=get_velocity)
    print(data[-1])
    print(f"Galaxy {data[-1][0]} has the max velocity of {data[-1][1]}km/sec.")
    print(f"Galaxy {data[0][0]} has the min velocity of {data[0][1]}km/sec.")


# random list
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key

# print list
# print('Sorted list:', random)