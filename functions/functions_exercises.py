##################### Q1 ##################### ✅
# takes temperature in fahrenheit, returns temp in celsius
# To convert temperatures in degrees Fahrenheit to Celsius, subtract 32 and multiply by .5556 (or 5/9).
#
# Input temp_in_f 32 *incorrect solution attempt*
# Output: 0.0
# def convert_f_to_c(f):
#     celsius_result = f - 32 * .5556
#     return celsius_result
# print(convert_f_to_c(32))
#     # This returns 14.2208. The math must be incorrect

# def convert_f_to_c(f):  *incorrect solution attempt*
#     celsius_result = f - 32 * 5/9
#     return celsius_result
# print(convert_f_to_c(32))
#     # This returns 14.22222222221. 

# def convert_f_to_c(f):  *incorrect solution attempt*
#     celsius_result = f - 30 / 2
#     return celsius_result
# print(convert_f_to_c(32))
#     # This returns 17.0. 

# def convert_f_to_c(f): ✅
#     celsius_result = (f - 32) / 1.8
#     return celsius_result
# print(convert_f_to_c(32))


# Input temp_in_f 0 ✅
# Output: -17.7777777777777778
# def convert_f_to_c(f): 
#     celsius_result = (f - 32) / 1.8
#     return celsius_result
# print(convert_f_to_c(0))

# Input temp_in_f 350 ✅ (except my math didn't get the 9 at the end.)
# Output: 176.6666666666666666669
# def convert_f_to_c(f): 
#     celsius_result = (f - 32) / 1.8
#     return celsius_result
# print(convert_f_to_c(350))

##################### Q2 ##################### ✅
# Accepts one parameter (integer),
# returns True when param is odd 
# and False when param is is even
#
# Input: num 2 ✅
# Output: False
# def odd_or_even(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
# print(odd_or_even(2))

# Input: num 7 ✅
# Output: True
# def odd_or_even(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
# print(odd_or_even(7))

# Input: num -1 ✅
# Output: True
# def odd_or_even(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
# print(odd_or_even(-1))

##################### Q3 ##################### 🍎
# Write a function that returns the mean of a list of numbers
#
# Input: numbers [4, 3, 2, 6] 🍎
# Output: 3.75
def calculate_mean(arr):
    count = 0
    for count in calculate_mean:
        count += 1
    print(count)
calculate_mean([4, 3, 2, 6])

# random_numbers = [-3, -5, 9, 1]
# count = 0
# for count in random_numbers:
#     count += 1
# print(count)

# Input: numbers [10, 5, 6] 🍎
# Output: 7.0

##################### Q4 ##################### 🍎
# Takes two params, the unit price of an item and how many unites were purchased 
# return the total cost, as a string
#
# Input: price_per_unit 4.25 🍎
# Input: num_units 3
# Output: $12.75

# Input: price_per_unit 3.79 🍎
# Input: num_units 3
# Output: $3.79

# Input: price_per_unit 1.49 🍎
# Input: num_units 7
# Output: $10.43