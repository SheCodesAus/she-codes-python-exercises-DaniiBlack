# The dictionary below represents the cost of individual items in a supermarket.
# A separate dictionary is given in the table below, this dictionary represents the quantity of each item purchased.
# Use these two dictionaries to write a program that outputs the cost of each item.

# Input: see 'quantity'
## Expected output:
# 1 Baby Spinach @ $2.78 = $2.783
# 3 Hot Chocolate @ $3.7 = $11.102
# 2 Crackers @ $2.1 = $4.201
# 1 Bacon @ $9.0 = $9.004
# 4 Carrots @ $0.56 = $2.242
# 2 Oranges @ $3.08 = $6.16

prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}



# Input: See quantity 
# quantity = {
#     "Baby Spinach": 2,
#     "Hot Chocolate": 1,
#     "Crackers": 4,
#     "Bacon": 0,
#     "Carrots": 8,
#     "Oranges": 5
# }
## Expected output:
# 2 Baby Spinach @ $2.78 = $5.56
# 1 Hot Chocolate @ $3.7 = $3.70
# 4 Crackers @ $2.1 = $8.40
# 0 Bacon @ $9.0 = $0.00
# 8 Carrots @ $0.56 = $4.48
# 5 Oranges @ $3.08 = $15.40