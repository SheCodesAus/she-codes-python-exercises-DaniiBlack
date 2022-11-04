################## FOR LOOPS ##################

################## Q1 ##################
# Ask user for a number. Use a for loop to print the times tables for that number
# Teachers solution: 
# num = input("Enter a number:")

# for i in range(1, num+1):
#     mult = i * num
#     print(f"{num}i * {i} = {mult}")
#
## Input 3 ✅
## Output: Enter a number: 3
### Output: 3 * 1 = 3, 3 * 2 = 6... etc
# num = int(input("Give me a number: "))
# print(f"You entered {num}. Times tables as follow: ")
# for count in range(1, 11):
#     print(num, 'x', count, '=', num * count)
#
## Input 7 ✅ 
## Output: Enter a number: 7
### Output: 7 * 1 = 7, 7 * 2 = 14... etc
# num = int(input("Give me a number: "))
# print(f"You entered {num}. Times tables as follow: ")
# for count in range(1, {num}):
#     print(num, 'x', count, '=', num * count)
#
# num = int(input("Give me a number: "))
# print(f"You entered {num}. Times tables as follow: ")
# val = range(num)
# for count in val:
#     print(num, 'x', count, '=', num * count)
#
## Input 0 ✅
## Output: Enter a number: 0

# num = int(input("Give me a number: ")) 🍎 returned the table instead of a single zero.
# print(f"You entered {num}. Times tables as follow: ")
# for count in range(1, 11):
#     print(num, 'x', count, '=', num * count)

# num = int(input("Give me a number: ")) ✅
# print(f"You entered {num}: ")
# val = range(num)
# for count in val:
#     print(num, 'x', count, '=', num * count)


################## Q2 ##################
# Ask user for a number. Use a for loop to sum from 0 to that number
## Input 3 ✅
## Output 6
# q = int(input("Enter a number: "))
# # print(f"Enter a number: {q} ")
# val = range(q + 1)
# i = 0
# for num in val:
#     i += num
# print(i)

## Input: 6 ✅
## Output: 21
# input = int(input("Enter a number: "))
# val = range(input + 1)
# i = 0
# for num in val:
#     i += num
# print(i)

## Input 0 ✅
## Output 0
# input = int(input("Enter a number: "))
# val = range(input + 1)
# i = 0
# for num in val:
#     i += num
# print(i)

################## Q3 ##################
# Given a list, use a for loop to sum all the numbers in the list
## Input: random_numbers = [3, 5, 9, 1]  ✅
## Output: 18
# Teachers solution: 
####### random_numbers = [3, 5, 9, 1]
####### sum = 0
######
####### for number in random_numbers:
#######     sum = sum + number 
#######     # or alternative syntax is: sum += number
#######     print(sum)
# random_numbers = [3, 5, 9, 1]
# i = 0
# for num in random_numbers:
#     i += num
# print(i)


## Input: random_numbers = [-3, -5, 9, 1]
## Output: 2 ✅
# random_numbers = [-3, -5, 9, 1]
# count = 0
# for count in random_numbers:
#     count += 1
# print(count)

## Input random_numbers = []
## Output 0 ✅
# random_numbers = []
# count = 0
# for count in random_numbers:
#     count += 1
# print(count)

################## Q4 ##################
# Use a for loop to format and print the provided list.
## Output ✅
# Teachers solution: 
####### random_numbers = [3, 5, 9, 1]
####### sum = 0
###### advice, print the initial item, to get a sense for what you're building on a for loop so you can keep iterating on it 
####### for item in mailing_list:
#######     name = item[0]
#######     email = item[1]
#######     print(f"{name}: {email}")
#######     sum = sum + number 
#######     # or alternative syntax is: sum += number
#######     print(sum)
# mailing_list = [
# ["Chilli", "chilli@thechihuahua.com"],
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Ivy", "noreply@goldendreamers.xyz"],
# ]
# for len in mailing_list:
#     print(f"{len[0]}: {len[1]}")