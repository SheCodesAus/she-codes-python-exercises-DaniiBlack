##### FOR LOOPS #####
# Objectives:
#   Understand how to use for and while loops
#   Understand what situations loops are useful in

#   my_iterable = [1, 2, 3]
#   for item in my_iterable:
#       # some code here
#       print(item)

#   for num in range(10):
      # range (which is a generator.) is indices exclusive, above number, will be the num inside, but not inclusive of 10.
      # an example is to use range(1, 10)
      # which will factor number 1, and not number 10.
      # another is to 'step'. Eg,
      # range(1, 10, 2)
      # the final number in there, will act as a "skip every nth" num
      # print(num)

# Challenge
# 1. Use a for loop to print numbers 0 to 100 (inclusive)
# for num in range(101):
#     print(num)

# 2. Use a for loop to print the numbers 0 to 100 in steps of 5 (5, 10, 15, etc..)
# for num in range(0, 101, 5):
#     print(num)
# step requires a start. range([step-start] [step-stop] [step])

##################################
## Challenge
# Demonstrate How to use a for loop to repeat code for every item in a list

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
# for item in range(len(chilli_wishlist)):
#     print(chilli_wishlist[item])
#     for item in chilli_wishlist:
#         print(f"Chilli wants: {item}")

##################################
## Challenge
# Adapt the for loop to print a message for each item in the list, e.g. “Chilli wants: item”.
# Use a for loop to print each item in a list from a previous exercise or example
# Demonstrate Nested for loops 

# chilli_wishlist = [
#     ["igloo"],
#     ["donut toy", "tennis ball", "crocodile toy"],
#     ["chicken", "peanut butter"],
#     ["cardboard box", "kong", "dig mat"]
# ]
# for category in chilli_wishlist:
#     for item in category:
#         print(item)
# category and item are python 

##### WHILE LOOPS #####
# Demonstrate: How to use a while loop to repeat code until a certain condition is me
guess = ""
while guess != "a":
    guess = input("Guess a letter: ")

# some_boolean_condition = false
# while some_boolean_condition


counter = 10
while counter <= 10:
    print(counter)
    counter = counter + 1
    # python notation = 
    # counter += 1 (js ++ I think?)