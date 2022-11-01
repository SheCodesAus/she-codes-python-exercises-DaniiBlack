                    # 0    1           2           3
# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
                    #-4     -3         -2           -1

# ensure indices are in correct order even when thinking "backward"
# indexing 
# print(len(chilli_wishlist))
# print(len(chilli_wishlist[4]))

# print(chilli_wishlist[0])
# print(chilli_wishlist[1])

# print(chilli_wishlist[-1])
# comes back with cardboard box

# slicing (will read from, you can use this to create another array, without editing the original array)
# https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf
# print(chilli_wishlist[0:2])
# igloo, chicken

# also slicing. 
# [this:notation] will provide a start and stop(before, not inclusive)
# print(chilli_wishlist[1:3])
# chicken, donut toy

# print(chilli_wishlist[1:3])
# print(chilli_wishlist[-3])

# chilli_wishlist.append('dog mat')
# item appends to end of list.
# chilli_wishlist.extend(['kong', 'tennis ball', 'crocodile toy'])
# multiple items appended (or EXTEND) to end of list
# chilli_wishlist.insert(1, 'peanut butter')
# item inserted to beginning of list

# pop will remove / edit the original array. You can "pop" into a new variable.
# chilli_wishlist.pop()
# chilli_wishlist.pop(2)

# chilli_wishlist.remove('tennis ball')
# print(chilli_wishlist)

# Set a small challenge similar to the example you walked through,
# some ideas:
# Add a new item to position -2
# Remove the third item from the list
# Add four new items to the end of the list.
# Remove the “igloo” item from the list


# Logic with lists.
# Demonstrate:
# - Perform simple logic using lists
# if "tennis ball" in chilli_wishlist:
#     print("Chilli would like a tennis ball.")
# else:
#     print("Chilli doesn't feel like playing fetch.")

# if len(chilli_wishlist) > 8:
#     print("Chilli wants a lot of stuff!")

# if "blue berries" not in chilli_wishlist:
#     chilli_wishlist.extend(["blue berries"])
#     print(chilli_wishlist)

#     print("add blue berries to chilli_wishlist please!")

# else:
#     chilli_wishlist.extend(["blue berries"])
#     print(chilli_wishlist)

# Teachers example
    # if not "blueberries" in chilli_wishlist:
    #     chilli_wishlist.append("blueberries")

# QUESTION: Do you have to escape the if statement? Example above, does not use any else or elif..
# I think print is like return, which takes you(/the code monsters) out of the if statement anyway. 

chilli_wishlist = [
    ['igloo'], # bed
    ['donut toy', 'tennis ball', 'crocodile toy'], # toys
    ['chicken', 'peanut butter'], # treats 
    ['cardboard box', 'kong', 'dig mat'] # activity based toys
]

# print(chilli_wishlist[2])
# prints array at index 2
# print(chilli_wishlist[2][1])
# prints item at index1 of array at index 2
# print(chilli_wishlist[2][1][0])
# prints P  index of subarray, index of item inside subarray, index of char in previous resulting item
# examples 
# peanut_butter = ["p", "e", "a", '...']
# name = "Naomi"
# print(name[0])

# Got stuck on this one:
# chilli_wishlist[2].insert[1](3, 'third item')
# print(chilli_wishlist[2])

# Use indexing to change the thid item in the second list
chilli_wishlist[2].append("Hello World")
print(chilli_wishlist[2])

# Add another sublist to the list
chilli_wishlist.append(["Goodbye", "World", "!"])
print(chilli_wishlist)