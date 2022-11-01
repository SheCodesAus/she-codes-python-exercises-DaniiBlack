# for loops
# Objectives:
#   Understand how to use for and while loops
#   Understand what situations loops are useful in

# my_iterable = [1, 2, 3]
# for item in my_iterable:
#     # some code here
#     print(item)

# for num in range(10):
    # range (which is a generator.) is indices exclusive, above number, will be the num inside, but not inclusive of 10.
    # an example is to use range(1, 10)
    # which will factor number 1, and not number 10.
    # another is to 'step'. Eg,
    # range(1, 10, 2)
    # the final number in there, will act as a "skip every nth" num
    # print(num)
##################################
## Challenge
# 1. Use a for loop to print numbers 0 to 100 (inclusive)
# for num in range(101):
#     print(num)

# 2. Use a for loop to print the numbers 0 to 100 in steps of 5 (5, 10, 15, etc..)
# for num in range(0, 101, 5):
#     print(num)
# step requires a start. range([step-start] [step-stop] [step])