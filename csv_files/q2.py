import csv

with open("colours_20_simple.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        print(f'{line[2]:<20}', f'{line[1]:<20}', f'{line[0]:<20}')