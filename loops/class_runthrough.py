## 8 November 2022
# # ## Why for_loop vs while loop
# # 
name_list = ['joy', 'bunny', 'aishwarya', 'kitty']
# ## access one
# print(f"hi {name_list[0]}")
# ## access multiple, option1
# print(f"hi {name_list[0]}")
# print(f"hi {name_list[1]}")
# print(f"hi {name_list[2]}")
# print(f"hi {name_list[3]}")

# In this example ^ we know exactly how many times to run this code,
# there are four names. 

###### for loop ######
# for name in name_list:
#     print(f"hi {name}")
#     input("--------")

###### while loop ######
# while some_condition_is_true:
    # do stuff
# (we want to run it until there's no more items in the list (in this example, the names_list))
# this means, we need a counter, to keep track of when we get to the end of the list. 

# counter = 0
# while counter < len(name_list):
#     # do stuff
#     # print(counter) to see what the loop is doing - proactive debugging, so to speak
#     name = name_list[counter]
#     print(f"hi {name}")
#     counter = counter + 1
#     input("--------")

# ## Example two
# ### To do wothout a looop - exmploe of whyyy we should use a loop
import random # a module available to use to 'randomise' numbers
budget = 100 # dollars
how_much_spent = 0 # dollars 

def buy_stuff():
    cost_of_item = random.randint(0,20)
    return cost_of_item

# -- If statement eg --
# how_much_spent += buy_stuff()
# print(f"total spent: {how_much_spent}")

# if how_much_spent < budget:
#     how_much_spent += buy_stuff()
#     print(f"total spent: {how_much_spent}")
# # repeat above code block, without a loop this would have to be repeated. 
# -- FOR LOOP EG --
# for i in range(0,100):
#     how_much_spent += buy_stuff()
#     print(f"total spent: {how_much_spent}")

#     input("--------")
#     if how_much_spent > budget:
#         break
# -- While loop --

while how_much_spent< budget:
    how_much_spent += buy_stuff()
    print(f"total spent: {how_much_spent}")
    input("--------")

