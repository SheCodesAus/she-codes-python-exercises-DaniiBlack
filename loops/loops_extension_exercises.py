################## LOOPS EXTENSION ##################
# Note: also python has a built in alignment for strings. if you add :<20 to your f-string variable like this:
# {groceries[items][0]:<20} will 

################## Q1 ##################
# Below is a list of foods and their prices per unit:
# groceries = [
#       ["Baby Spinach", 2.78],
#       ["Hot Chocolate", 3.70],
#       ["Crackers", 2.10],
#       ["Bacon", 9.00],
#       ["Carrots", 0.56],
#       ["Oranges", 3.08]
# ]
# Ask the user how many units of each item they bought, then output the corresponding receipt.
# For the input below, assume that the input is provided in the same order as defined in the list above.
# # ========Izzy's Food Emporium========
# # Input: 1        Output: Baby Spinach    $2.78
# # Input: 3        Output: Hot Chocoloate  $11.10
# # Input: 2        Output: Crackers        $4.20
# # Input: 1        Output: Bacon           $9.00
# # Input: 4        Output: Carrots         $2.24
# # Input: 2        Output: Oranges         $6.16
# # =======================================================

# Teachers solution 
# item = ["Baby Spinach", 2.78]   Teacher noted to add notes here to keep in mind what the thing you're working on is. (above first line of the for loop.)
# groceries = [
#       ["Baby Spinach", 2.78],
#       ["Hot Chocolate", 3.70],
#       ["Crackers", 2.10],
#       ["Bacon", 9.00],
#       ["Carrots", 0.56],
#       ["Oranges", 3.08]
# ]
# This is broken for some reason - to debug, later:
# sum = 0
# for item in groceries: 
#     name_of_item = item[0]
#     num_items = int(input(f"How many of {name_of_item}? "))
#     price_per_unit = item[1]
#     cost_of_item = num_items * price_per_unit
#     item.append(cost_of_item)
#     sum += cost_of_item
#     # print(item)

#     print("========Izzy's Food Emporium========")
#     for item in groceries:
#         name = item[0]
#         cost = item[2]
#         print(f"{name}\t{cost:.2f}")
#         print("================================")
#         print(f"\t\t${sum}")


################## Q2 ##################
# Ask the user to enter a string. Output the string one character at a time, as well as it’s position in the string.
# Input: cats  
# Output: "Please enter a string: " 0 c, 1 a, 2 t, 3 s
# string_input = input("Please enter a string: ")
# counter = 0
# for letter in string_input:
#     print(f"{counter} {letter}")
#     counter += 1

################## Q3 ##################
# Ask the user for a number and use this to generate a pyramid of that height.
# Input 5
# Pyramid size: 5
# *
# **
# ***
# ****
# *****
number = 5

for pyramid_row in range(5):
    # print(pyramid_row)
    pyramid_row_output = "*" * (pyramid_row+1)
    print(pyramid_row_output)

################## Q4 ##################
# Ask the user for a number and use this to generate a (different) pyramid of that height.
# Input: 5
# Output: 
# "Pyramid size: 5"
#     *
#     **
#     ***
#     ****
#     *****
# Lol. in the actual pyramid shape though. ^^ smh