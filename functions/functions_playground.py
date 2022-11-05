##################### FUNCTIONS #####################
# Learning Objectives:
# - Be able to write and call a function
# - Understand variable scope 
# - Understand the purpose of a function 
# Demonstrate: 
# - How to write and call a function  

###################### Section 1 ######################

# Function syntax 
# def name_of_function():
#     '''
#     docstring explains function
#     this is a function that says "hello"!
#     '''
#     print("hello!")
#     name_of_function()
# Demonstarte a function: 
# def create_greeting(name):
#     greeting = f"Hello, {name}"
#     # print(greeting)
#     return greeting
# print(create_greeting("Chilli"))
# print(create_greeting("Ivy"))
# print(create_greeting("Remus"))
# # create_greeting('Joy')

# Another teacher example: 
# def add_function(num1, num2):
#     sum = num1 + num2
#     return sum
#     # print(f"printing sum from function: {sum}")
# # add_function(1, 2) -- no good, see next line..
# result_of_function = add_function(1, 2)
# print(result_of_function)

########## Challenge 1 ########## ✅
# Create another function that takes an integer as a parameter and returns that integer multiplied by 3.
# def multiply_function(num1, num2):
#     sum = num1 * num2
#     return sum
# result_of_function = multiply_function(5, 5)
# print(result_of_function)
# ---------------
# Teachers example: 
# def multiply_by_three(num):
    # output = num * 3 # without returning this, (line below), this will only save into variable, "output"
    # return output

    # result = multiply_by_three(5)
    # print(output)
###################### Section 2 ######################
# Demonstrate:
# - That variable created in a function exists only in that function.

# Example: 
# def convert_cm_to_in(length_cm):
#     length_in_inches = length_cm / 2.54
#     return length_in_inches    
# print(convert_cm_to_in(20))

# Demonstrate that variables created in a function, exist only in that function. #
# Example:
# def convert_cm_to_in(length_cm):
#     length_in_inches = length_cm / 2.54
#     print(length_in_inches)
#     return length_in_inches

#     length_of_closet_in_inches = convert_cm_to_in(50)
#     print(length_of_closet_in_inches)
#     space_left_in_room = 50 - length_of_closet_in_inches
# print(length_in_inches)

# another example function: 
# def convert_cm_to_in(length_cm):
#     length_in_inches = length_cm / 2.54
#     return length_in_inches
# 
# print(length_in_inches) # does not exist in this scope. 
# length_in_cms = 20
# print(convert_cm_to_in(length_in_cms))

########## Challenge 2 ########## ✅
# Write a function similar to that above, that converts inches to centimeters. 
# def in_to_cm(length_in):
#     length_in_cm = length_in * 2.54
#     return length_in_cm
# print(in_to_cm(20))

# Note: These functions are running on the assumption that we are going to give it the appropriate thing to consume (in this case above, int or float maybe? for conversion. We haven't started learning how to set types/ restrictions/ throw errors etc 

###################### Section 3 ######################
# Demonstrate A function with multiple parameters 
# Example:
# def return_mean(a, b):
#     total = a + b
#     mean = total / 2
#     return mean

# def prints_mean(a, b):
#     total = a + b
#     mean = total / 2
#     print(mean)

# result_return = return_mean(3, 4)
# result_prints = prints_mean(3, 4)

# print("===============")
# print(result_return)
# print(result_print)