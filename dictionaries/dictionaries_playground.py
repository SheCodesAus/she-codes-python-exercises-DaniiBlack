####### Dictionaries #######
# Learning Objectives:
# ● Understand what a dictionary is.
# ● Understand suitable use cases for a dictionary.
# ● Be able to create and populate a dictionary.

# Introduction #
# Give a brief (verbal) description of what a dictionary is.
# Explain the concept of key/value pairs.

# Demonstrate:
# 1. How to create a dictionary.
# 2. How to update a dictionary.
# 3. How to retrieve data from a dictionary.

# For example:
# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Bacon": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08,
#     }
# print(groceries)
## looking at a specific value ##
#   print(groceries["Baby Spinach"])
#
## adding a new item ##
#   groceries["Avocadoes"] = 1.00
#   print(groceries)

## changing the value of an existing item ##
#   groceries["Hot Chocolate"] = 2.70
#   print(groceries)

## removing an item from the dictionary ##
#   del groceries["Crackers"]
#   print(groceries)

## iterating over the dictionary ##
#    for item in groceries:
#      print(f"{item}: ${groceries[item]}")
#    print()

## another way to iterate over the dictionary ##
#   for item, price in groceries.items():
#     print(f"{item}: ${price}")