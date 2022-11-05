import csv

# with open('2016_pilbara.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)
## Outputs the contents of the pilbarra file ^ 

population = []
with open("2016_pilbara.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        population.append(line)
        
print(population)
print()

for age_group in population: 
    print(f"{age_group[0]} {age_group[1]}")

# Writing to csv file 
with open("population.csv", mode="w", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=",")

    for age_group in population:
        csv_writer.writerow([age_group[1], age_group[0]])
# delimiter - the thing that seperates the value *COMMA SEPERATED VALUES*
# Although, you can use semi-colons too and probably others, but comma would be best unless specified otherwise. 